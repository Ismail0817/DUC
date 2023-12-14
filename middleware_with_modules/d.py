# server.py
import socket

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")

      
        # Wait for a connection
        print("Waiting for a connection...")
        client_socket, client_address = server_socket.accept()
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
        server_socket.close()

if __name__ == "__main__":
    host = "127.0.0.1"  # Change this to your desired host
    port = 12345         # Change this to your desired port
    start_server(host, port)