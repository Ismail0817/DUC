# program2.py
from flask import Flask, jsonify, request

def perform_work_on_data_fog(data):
    # logic to process data in Program 2
    return f"Processed by fog: {data.upper()}"

app = Flask(__name__)

@app.route('/communicate_with_fog', methods=['POST'])
def communicate_with_fog():
    data_from_middleware = request.json['data']
    
    # Perform some computation on the data
    processed_data_fog = perform_work_on_data_fog(data_from_middleware)
    
    # Return processed data to the middleware
    return jsonify({"result": processed_data_fog})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
