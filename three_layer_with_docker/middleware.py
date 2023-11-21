from flask import Flask, request, jsonify
import requests 

import docker
import time

client = docker.from_env()

# client.containers.run("test3:1.0", detach=True)

# client.containers.list()

# Define the port mapping (container_port:host_port)
# port_mapping = {"5000/tcp": 5000}
# container = client.containers.run("test3:1.0", detach=True, ports=port_mapping)
# print(container.status)

# time.sleep(5)


app = Flask(__name__)

def communicate_with_fog(data):
    # logic to send data to fog

    port_mapping = {"5001/tcp": 5001}
    container = client.containers.run("program2:1.0", detach=True, ports=port_mapping)
    print(container.status)

    time.sleep(5)

    response = requests.post("http://localhost:5001/communicate_with_fog", json={"data": data})
    return response.json()["result"]

def communicate_with_cloud(data):
    # logic to send data to cloud

    port_mapping = {"5002/tcp": 5002}
    container = client.containers.run("program3:1.0", detach=True, ports=port_mapping)
    print(container.status)

    time.sleep(5)

    response = requests.post("http://localhost:5002/communicate_with_cloud", json={"data": data})
    return response.json()["result"]

@app.route('/process_data', methods=['POST'])
def process_data():
    # initialize a variable with data from Edge
    data_from_edge = request.json['data']
    
    # Send data to Fog and receive the computed data in a variable
    processed_data_fog = communicate_with_fog(data_from_edge)
    
    # Send processed data from Fog to Cloud
    processed_data_cloud = communicate_with_cloud(processed_data_fog)
    
    # Return final processed data to Program 1
    return jsonify({"result": processed_data_cloud})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
