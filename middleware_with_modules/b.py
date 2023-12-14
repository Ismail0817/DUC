# client.py
import socket
import time

def send_data(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        counter = 1
        while True:
            data_to_send = f"Data from client: {counter}"
            client_socket.sendall(data_to_send.encode('utf-8'))
            print(f"Sent: {data_to_send}")

            time.sleep(1)
            counter += 1

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    server_host = "127.0.0.1"  # Change this to the server's host
    server_port = 12345         # Change this to the server's port
    send_data(server_host, server_port)
