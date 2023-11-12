from flask import Flask, request, jsonify
import requests 

app = Flask(__name__)

def communicate_with_program_2(data):
    # logic to send data to Program 2
    response = requests.post("http://localhost:5001/communicate_with_program_2", json={"data": data})
    return response.json()["result"]

def communicate_with_program_3(data):
    # logic to send data to Program 3
    response = requests.post("http://localhost:5002/communicate_with_program_3", json={"data": data})
    return response.json()["result"]

@app.route('/process_data', methods=['POST'])
def process_data():
    # initialize a variable with data from program 1
    data_from_program_1 = request.json['data']
    
    # Send data to Program 2 and receive the computed data in a variable
    processed_data_2 = communicate_with_program_2(data_from_program_1)
    
    # Send processed data from program 2 to Program 3
    processed_data_3 = communicate_with_program_3(processed_data_2)
    
    # Return final processed data to Program 1
    return jsonify({"result": processed_data_3})

if __name__ == '__main__':
    app.run(port=5000)
