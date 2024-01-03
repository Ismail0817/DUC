import socket
import threading
import requests
import time

class Fog:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(1)
            print(f"fog listening on {self.host}:{self.port}")

            # Wait for a connection
            print("fog Waiting for a connection...")
            client_socket, client_address = self.server_socket.accept()

            print(f"fog Connected to {client_address}")

            while True:
                # Receive data from the client
                data = client_socket.recv(1024)
                if not data:
                    break  # Break the loop if no data is received
                print(f"fog Received data: {data.decode('utf-8')}")

            # Close the connection
            client_socket.close()

        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.server_socket.close()
            self.commmunicate_with_cloud()
            

    def commmunicate_with_cloud(self):
        # negotiation and orchetration
        response_from_middleware = requests.post("http://localhost:5000/api_fog", json={"function": "deploy_in_cloud", "name": "process1"})
        print(response_from_middleware.json()["result_negotiate"])

        # socket open
        response_from_middleware = requests.post("http://localhost:5000/api_fog", json={"function": "open_socket", "name": "process1"})
        print(response_from_middleware.json()["result"])
        host = response_from_middleware.json()["host"]
        port = response_from_middleware.json()["port"]

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client_socket.connect((host, port))
            print(f"Connected to middleware at {host}:{port}")

            counter = 1
            while counter < 6:
                data_to_send = f"Data: {counter}"
                client_socket.sendall(data_to_send.encode('utf-8'))
                print(f"Sent: {data_to_send}")

                time.sleep(2)
                counter += 1

        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()