from data_handler import DataHandler


host = "127.0.0.1"  # Change this to your desired host
port = 12345         # Change this to your desired port

server_instance = DataHandler(host, port)
server_instance.start_server()