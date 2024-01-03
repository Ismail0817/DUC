# orchestrator.py

import threading
from cloud import Cloud


class Orchestrator:
    def __init__(self, cloud_host, cloud_port):
        self.cloud_host = cloud_host
        self.cloud_port = cloud_port

    def orchestrate_pods(self):
        # Add logic to orchestrate Kubernetes pods based on the request

        socket_opener = threading.Thread(target=self.open_socket_cloud, args=(self.cloud_host, self.cloud_port))
        socket_opener.start()

        return ("true")

    def open_socket_cloud(self,cloud_host, cloud_port):
        cloud = Cloud(cloud_host, cloud_port)
        cloud.start_server()