import socket
import threading
import requests

from cloud import Cloud

class DataHandler:
    def __init__(self, host, port, cloud_host, cloud_port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.cloud_host = cloud_host
        self.cloud_port = cloud_port
        # cloud = Cloud(cloud_host, cloud_port)
        # cloud.start_server()

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(1)
            print(f"edge Middleware data handler listening on {self.host}:{self.port}")

            # Wait for a connection
            print("edge Middleware data handler Waiting for a connection...")
            
            response_from_fog_middleware = requests.post("http://localhost:5000/api_fog", json={"function": "open_socket_for_edge", "name": "process1"})
            print(response_from_fog_middleware.json()["result"])
            fog_middleware_host = response_from_fog_middleware.json()["host"]
            fog_middleware_port = response_from_fog_middleware.json()["port"]

            client_socket, client_address = self.server_socket.accept()

            print(f"edge Middleware data handler Connected to {client_address}")

            # socket_opener = threading.Thread(target=self.open_socket_cloud, args=(self.cloud_host, self.cloud_port))
            # socket_opener.start()

            cloud_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cloud_socket.connect((fog_middleware_host, fog_middleware_port))
            print(f"Connected to fog middleware at {self.cloud_host}:{self.cloud_port}")

            while True:
                # Receive data from the client
                data = client_socket.recv(1024)
                if not data:
                    break  # Break the loop if no data is received
                print(f"edge Middleware Received data: {data.decode('utf-8')}")
                cloud_socket.sendall(data)
                print(f"edge Middleware Send data: {data.decode('utf-8')}")


            # Close the connection
            client_socket.close()
            cloud_socket.close()

        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.server_socket.close()

    # def open_socket_cloud(self,cloud_host, cloud_port):
    #     cloud = Cloud(cloud_host, cloud_port)
    #     cloud.start_server()

    
    # def send_data_to_cloud(self,host, port, data):
    #     cloud_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #     try:
    #         cloud_socket.connect((host, port))
    #         print(f"Connected to middleware at {host}:{port}")

            
    #         data_to_send = f"Data: {data}"
    #         cloud_socket.sendall(data_to_send.encode('utf-8'))
            

    #     except Exception as e:
    #         print(f"Error: {e}")
    #     finally:
    #         cloud_socket.close()