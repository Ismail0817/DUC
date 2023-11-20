import socket
import pickle

# Create a socket to listen for connections from Program 1
server_socket_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address_1 = ('localhost', 5000)
server_socket_1.bind(server_address_1)
server_socket_1.listen(1)

print("Middleware is waiting for Program 1...")

# Accept a connection from Program 1
connection_1, client_address_1 = server_socket_1.accept()
print("Connected to Program 1:", client_address_1)

# Create a socket to connect to Program 2
program2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
program2_address = ('localhost', 7000)
program2_socket.connect(program2_address)

# Receive data from Program 1
data_from_program1 = pickle.loads(connection_1.recv(1024))
# Perform any necessary middleware processing on data_from_program1

# Send data to Program 2
program2_socket.sendall(pickle.dumps(data_from_program1))

# Receive modified data from Program 2
modified_data_from_program2 = pickle.loads(program2_socket.recv(1024))
# Perform any necessary middleware processing on modified_data_from_program2

# Send the modified data back to Program 1
connection_1.sendall(pickle.dumps(modified_data_from_program2))

# Close connections
connection_1.close()
server_socket_1.close()
program2_socket.close()
