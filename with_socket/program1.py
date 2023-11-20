import socket
import pickle

# Create a socket to connect to the middleware
middleware_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
middleware_address = ('localhost', 6000)
middleware_socket.connect(middleware_address)

# Perform some work on the data (replace this with your specific logic)
original_data = "Data to be processed by Program 1"
print("Program 1 is processing data:", original_data)

# Send the processed data to the middleware
middleware_socket.sendall(pickle.dumps(original_data))

# Receive the final processed data from the middleware
final_data = pickle.loads(middleware_socket.recv(1024))
print("Program 1 received the final processed data:", final_data)

# Close the connection
middleware_socket.close()
