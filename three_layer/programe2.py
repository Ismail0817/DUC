# program2.py
from flask import Flask, jsonify, request

def perform_work_on_data_2(data):
    # logic to process data in Program 2
    return f"Processed by Program 2: {data.upper()}"

app = Flask(__name__)

@app.route('/communicate_with_program_2', methods=['POST'])
def communicate_with_program_2():
    data_from_middleware = request.json['data']
    
    # Perform some computation on the data
    processed_data_2 = perform_work_on_data_2(data_from_middleware)
    
    # Return processed data to the middleware
    return jsonify({"result": processed_data_2})

if __name__ == '__main__':
    app.run(port=5001)
