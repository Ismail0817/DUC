from flask import Flask, request, jsonify
import requests 

import socket
import threading

# import middleware modules
from negotiator import Negotiator
from orchestrator import Orchestrator
from data_handler_from_edge import DataHandler_from_edge
from data_handler import DataHandler

from deploy_req import Deploy

app = Flask(__name__)

@app.route('/api_fog', methods=['POST'])
def api():
    # initialize a variable with data from fog. Data got through api reequeest
    function_from_fog = request.json['function']
    name_from_fog = request.json['name']

    if function_from_fog == "negotiate":
        name_from_fog = Negotiator()
        result = name_from_fog.check_resources()
        return jsonify({"result": result})
    
    if function_from_fog == "orchestrate":
        name_from_fog = Orchestrator("127.0.0.1", 29914)
        result = name_from_fog.orchestrate_pods()
        return jsonify({"result": result})

    # # getting req from edge to negotiate in fog
    # if function_from_fog == "negotiate_fog":
    #     name_from_fog = Negotiator()
    #     result = name_from_fog.check_resources()
    #     return jsonify({"result": result})

    # # getting req from fog to negotiate in cloud
    # if function_from_fog == "negotiate_cloud":
    #     # name_from_fog = Negotiator()
    #     response_from_cloud_middleware = requests.post("http://localhost:5001/api_cloud", json={"function": "negotiate", "name": "process1"})
    #     # result = name_from_fog.check_resources()
    #     return jsonify({"result": response_from_cloud_middleware.json()["result"]})    

    if function_from_fog == "deploy_in_cloud":
        deploy = Deploy()
        # negotiate_response = deploy.negotiate()
        response_from_cloud_middleware = deploy.deploy_pods()
        # response_from_cloud_middleware = requests.post("http://localhost:5001/api_cloud", json={"function": "negotiate", "name": "process1"})
        # result = name_from_fog.check_resources()
        return jsonify({"result_negotiate": response_from_cloud_middleware})  
    
    # if function_from_fog == "orchestrate":
    #     name_from_fog = Orchestrator()
    #     result = name_from_fog.orchestrate_pods()
    #     return jsonify({"result": result})

    if function_from_fog == "open_socket":
        fog_middleware_host = "127.0.0.1"  
        fog_middleware_port = 12345    

        cloud_host = "127.0.0.1"
        cloud_port = 23314     

        # calling the dala handler module which will open a new socket to get data. it is done in 
        # new thread otherwise the code will get stuck here
        socket_opener = threading.Thread(target=open_socket, args=(fog_middleware_host, fog_middleware_port, cloud_host, cloud_port))
        socket_opener.start()
        return jsonify({"result": f"fog middleware socket opened on {fog_middleware_host}:{fog_middleware_port} ", "host": fog_middleware_host, "port": fog_middleware_port})
    
    if function_from_fog == "open_socket_for_edge":
        host = "127.0.0.1"  
        port = 14509    

        fog_host = "127.0.0.1"
        fog_port = 29914     

        # calling the dala handler module which will open a new socket to get data. it is done in 
        # new thread otherwise the code will get stuck here
        socket_opener1 = threading.Thread(target=open_socket_for_edge, args=(host, port, fog_host, fog_port))
        socket_opener1.start()
        return jsonify({"result": f"fog middleware socket opened on {host}:{port} ", "host": host, "port": port})
    
    return jsonify({"result": "no function found"})

def open_socket(host, port, cloud_host, cloud_port):
    data_handler = DataHandler(host, port, cloud_host, cloud_port)
    data_handler.start_server()


def open_socket_for_edge(host, port, fog_host, fog_port):
    data_handler = DataHandler_from_edge(host, port, fog_host, fog_port)
    data_handler.start_server()

if __name__ == '__main__':
    app.run(port=5000)