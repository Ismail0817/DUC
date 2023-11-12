from flask import Flask, request, jsonify
import requests 

app = Flask(__name__)

def communicate_with_fog(data):
    # logic to send data to fog
    response = requests.post("http://localhost:5001/communicate_with_fog", json={"data": data})
    return response.json()["result"]

def communicate_with_cloud(data):
    # logic to send data to cloud
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
    app.run(port=5000)
