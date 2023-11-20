import socket
import pickle

# Create a socket to listen for connections from the middleware
server_socket_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address_2 = ('localhost', 7000)
server_socket_2.bind(server_address_2)
server_socket_2.listen(1)

print("Program 2 is waiting for the middleware...")

# Accept a connection from the middleware
connection_2, client_address_2 = server_socket_2.accept()
print("Connected to Middleware:", client_address_2)

# Receive data from the middleware
data_from_middleware = pickle.loads(connection_2.recv(1024))
# Perform your specific work on data_from_middleware here

# Send the modified data back to the middleware
modified_data = "Data processed by Program 2"
connection_2.sendall(pickle.dumps(modified_data))

# Close connections
connection_2.close()
server_socket_2.close()
