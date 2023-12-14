import socket
import threading

class DataHandler:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(1)
            print(f"Server listening on {self.host}:{self.port}")

            # Wait for a connection
            print("Waiting for a connection...")
            client_socket, client_address = self.server_socket.accept()

            print(f"Connected to {client_address}")

            while True:
                # Receive data from the client
                data = client_socket.recv(1024)
                if not data:
                    break  # Break the loop if no data is received
                print(f"Received data: {data.decode('utf-8')}")

            # Close the connection
            client_socket.close()

        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.server_socket.close()