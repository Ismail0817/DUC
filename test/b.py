# middleware.py
from flask import Flask, request, jsonify
import requests  # Import the requests library


app = Flask(__name__)

def communicate_with_program_2(data):
    # Your logic to send data to Program 2
    # For example, let's assume it just adds a suffix
    response = requests.post("http://localhost:5001/communicate_with_program_2", json={"data": data})
    return response.json()["result"]

@app.route('/process_data', methods=['POST'])
def process_data():
    data_from_program_1 = request.json['data']
    
    # Step 3: Send data to Program 2
    processed_data_2 = data_from_program_1.upper()+"hello"
    
    # Step 5: Return processed data to Program 1
    return jsonify({"result": processed_data_2})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
