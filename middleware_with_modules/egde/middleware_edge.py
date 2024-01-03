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

@app.route('/api_edge', methods=['POST'])
def api_edge():
    # initialize a variable with data from fog. Data got through api reequeest
    function_from_edge = request.json['function']
    name_from_edge = request.json['name']

    # print(function_from_edge)

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

    if function_from_edge == "deploy_in_fog":
        # print("insidee function call")
        deploy = Deploy()
        # negotiate_response = deploy.negotiate()
        
        response_from_cloud_middleware = deploy.deploy_pods()
        # response_from_cloud_middleware = requests.post("http://localhost:5001/api_cloud", json={"function": "negotiate", "name": "process1"})
        # result = name_from_fog.check_resources()
        
        return jsonify({"result_negotiate": response_from_cloud_middleware})  
    
    if function_from_edge == "orchestrate":
        name_from_fog = Orchestrator()
        result = name_from_fog.orchestrate_pods()
        return jsonify({"result": result})

    if function_from_edge == "open_socket":
        edge_middleware_host = "127.0.0.1"  
        edge_middleware_port = 17445    

        fog_host = "127.0.0.1"
        fog_port = 29914     

        # calling the dala handler module which will open a new socket to get data. it is done in 
        # new thread otherwise the code will get stuck here
        socket_opener = threading.Thread(target=open_socket, args=(edge_middleware_host, edge_middleware_port, fog_host, fog_port))
        socket_opener.start()
        return jsonify({"result": f"edge middleware socket opened on {edge_middleware_host}:{edge_middleware_port} ", "host": edge_middleware_host, "port": edge_middleware_port})
    
    
    return jsonify({"result": "no function found"})

def open_socket(host, port, fog_host, fog_port):
    data_handler = DataHandler(host, port, fog_host, fog_port)
    data_handler.start_server()

if __name__ == '__main__':
    app.run(port=5002)