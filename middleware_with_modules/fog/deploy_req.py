# deploy.py
import requests 

class Deploy:
    def deploy_pods(self):
        # Add logic to send a request to the negotiator to deploy new pods
        # print ("send deploy req")
        negotiation_response_from_cloud_middleware = requests.post("http://localhost:5001/api_cloud", json={"function": "negotiate", "name": "process1"})
        print(negotiation_response_from_cloud_middleware.json()["result"])
        if negotiation_response_from_cloud_middleware.json()["result"] == "negotiation successful":
            orchestration_response_from_cloud_middleware = requests.post("http://localhost:5001/api_cloud", json={"function": "orchestrate", "name": "process1"})
            print(orchestration_response_from_cloud_middleware.json()["result"])
            if orchestration_response_from_cloud_middleware.json()["result"] == "true":
                return "orchestration in cloud successful"
            return "orchestration in cloud unsuccessful"
        return "negotiation unsuccessful"

    def negotiate(self):
        response_from_cloud_middleware = requests.post("http://localhost:5001/api_cloud", json={"function": "negotiate", "name": "process1"})
        return response_from_cloud_middleware
    def orchestrate(self):
        response_from_cloud_middleware = requests.post("http://localhost:5001/api_cloud", json={"function": "orchestrate", "name": "process1"})
        return response_from_cloud_middleware