# program3.py
from flask import Flask, jsonify, request

def perform_work_on_data_cloud(data):
    # logic to process data in cloud
    return f"Processed by cloud: {data}"

app = Flask(__name__)

@app.route('/communicate_with_cloud', methods=['POST'])
def communicate_with_cloud():
    data_from_middleware = request.json['data']
    
    # Perform some computation on the data
    processed_data_cloud = perform_work_on_data_cloud(data_from_middleware)
    
    # Return processed data to the middleware
    return jsonify({"result": processed_data_cloud})

if __name__ == '__main__':
    app.run(port=5002)
