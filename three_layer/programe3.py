# program3.py
from flask import Flask, jsonify, request

def perform_work_on_data_3(data):
    # logic to process data in Program 3
    return f"Processed by Program 3: {data}"

app = Flask(__name__)

@app.route('/communicate_with_program_3', methods=['POST'])
def communicate_with_program_3():
    data_from_middleware = request.json['data']
    
    # Perform some computation on the data
    processed_data_3 = perform_work_on_data_3(data_from_middleware)
    
    # Return processed data to the middleware
    return jsonify({"result": processed_data_3})

if __name__ == '__main__':
    app.run(port=5002)
