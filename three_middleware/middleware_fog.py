from flask import Flask, request, jsonify
import requests 
import programe2

app = Flask(__name__)

def communicate_with_fog(data):
    # logic to send data to fog
    response = programe2.perform_work_on_data_fog(data)
    return response

def communicate_with_cloud(data):
    # logic to send data to cloud
    response = requests.post("http://localhost:5000/process_data_in_cloud", json={"data": data})
    return response.json()["result"]
    # return response

@app.route('/process_data_in_fog', methods=['POST'])
def process_data_in_fog():
    # initialize a variable with data from Edge
    data_from_edge = request.json['data']
    
    # Send data to Fog and receive the computed data in a variable
    processed_data_fog = communicate_with_fog(data_from_edge)
    
    # Send processed data from Fog to Cloud
    processed_data_cloud = communicate_with_cloud(processed_data_fog)
    
    # Return final processed data to Program 1
    return jsonify({"result": processed_data_cloud})

if __name__ == '__main__':
    app.run(port=5006)
