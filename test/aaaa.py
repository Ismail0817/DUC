


import docker

client = docker.from_env()

# client.containers.run("test3:1.0", detach=True)

# client.containers.list()

# Define the port mapping (container_port:host_port)
port_mapping = {"5000/tcp": 5000}

# Run the Docker container with port mapping
container = client.containers.run("test3:1.0", detach=True, ports=port_mapping)



# Optionally, you can print the container ID
print("Container ID:", container.id)