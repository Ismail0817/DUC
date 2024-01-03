import socket
import threading

class DataHandler_from_edge:
    def __init__(self, host, port, fog_host, fog_port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.cloud_host = fog_host
        self.cloud_port = fog_port
        # cloud = Cloud(cloud_host, cloud_port)
        # cloud.start_server()

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(1)
            print(f"Fog Middleware listening on {self.host}:{self.port}")

            # Wait for a connection
            print("Fog Middleware Waiting for a connection...")
            client_socket, client_address = self.server_socket.accept()

            print(f"Connected to {client_address}")

            # socket_opener = threading.Thread(target=self.open_socket_cloud, args=(self.cloud_host, self.cloud_port))
            # socket_opener.start()

            cloud_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cloud_socket.connect((self.cloud_host, self.cloud_port))
            print(f"fog middleware Connected to fog at {self.cloud_host}:{self.cloud_port}")

            while True:
                # Receive data from the client
                data = client_socket.recv(1024)
                if not data:
                    break  # Break the loop if no data is received
                print(f"fog Middleware Received data: {data.decode('utf-8')}")
                cloud_socket.sendall(data)
                print(f"fog Middleware Send data: {data.decode('utf-8')}")


            # Close the connection
            client_socket.close()
            cloud_socket.close()

        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.server_socket.close()

    