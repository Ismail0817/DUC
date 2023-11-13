from flask import Flask, request, jsonify
import requests 
import programe3

app = Flask(__name__)

def communicate_with_cloud(data):
    # logic to send data to cloud
    # response = requests.post("http://localhost:5002/communicate_with_cloud", json={"data": data})
    response = programe3.perform_work_on_data_cloud(data)
    # return response.json()["result"]
    return response

@app.route('/process_data_in_cloud', methods=['POST'])
def process_data_in_cloud():
    # initialize a variable with data from Edge
    data_from_fog = request.json['data']
    
    # Send processed data from Fog to Cloud
    processed_data_cloud = communicate_with_cloud(data_from_fog)
    
    # Return final processed data to Program 1
    return jsonify({"result": processed_data_cloud})

if __name__ == '__main__':
    app.run(port=5000)
