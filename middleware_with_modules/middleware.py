# middleware.py

import socket
import threading

from negotiator import Negotiator
from orchestrator import Orchestrator
from data_handler import DataHandler
from deploy_req import Deploy

def handle_client(client_socket, client_address):
    try:
        print(f"Connected to {client_address}")
        negotiator = Negotiator()
        orchestrator = Orchestrator()
        data_handler = DataHandler()
        deploy = Deploy()
        while True:
            # Receive data from the client
            data = client_socket.recv(1024)
            if data=="close" or not data:
                break  # Break the loop if no data is received
            elif data == "deploy":
                deploy.deploy_pods()
            elif data == "negotiate":
                negotiator.check_resources()
            elif data == "orchestrate":
                orchestrator.orchestrate_pods()
            else:
                data_handler.pass_data()

            print(f"Received data: {data.decode('utf-8')}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print(f"Connection with {client_address} closed")

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server listening on {host}:{port}")

        while True:
            # Wait for a connection
            print("Waiting for a connection...")
            client_socket, client_address = server_socket.accept()

            # Start a new thread to handle the client
            client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_handler.start()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    host = "127.0.0.1"  # Change this to your desired host
    port = 12345         # Change this to your desired port
    start_server(host, port)

