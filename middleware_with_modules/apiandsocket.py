from flask import Flask, request, jsonify
import requests 

import socket
import threading

# import middleware modules
from negotiator import Negotiator
from orchestrator import Orchestrator
from data_handler import DataHandler
from deploy_req import Deploy

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    # initialize a variable with data from fog. Data got through api reequeest
    function_from_fog = request.json['function']
    name_from_fog = request.json['name']

    if function_from_fog == "negotiate":
        name_from_fog = Negotiator()
        result = name_from_fog.check_resources()
        return jsonify({"result": result})
    
    if function_from_fog == "orchestrate":
        name_from_fog = Orchestrator()
        result = name_from_fog.orchestrate_pods()
        return jsonify({"result": result})

    if function_from_fog == "open_socket":
        host = "127.0.0.1"  
        port = 12345         

        # calling the dala handler module which will open a new socket to get data. it is done in 
        # new thread otherwise the code will get stuck here
        socket_opener = threading.Thread(target=open_socket, args=(host, port))
        socket_opener.start()
        return jsonify({"result": f"socket opened on {host}:{port} ", "host": host, "port": port})
    
    
    return jsonify({"result": "no function found"})

def open_socket(host, port):
    data_handler = DataHandler(host, port)
    data_handler.start_server()

if __name__ == '__main__':
    app.run(port=5000)