# orchestrator.py

import threading
from fog import Fog


class Orchestrator:
    def __init__(self, fog_host, fog_port):
        self.fog_host = fog_host
        self.fog_port = fog_port

    def orchestrate_pods(self):
        # Add logic to orchestrate Kubernetes pods based on the request

        socket_opener = threading.Thread(target=self.open_socket_cloud, args=(self.fog_host, self.fog_port))
        socket_opener.start()

        return ("true")

    def open_socket_cloud(self,fog_host, fog_port):
        fog = Fog(fog_host, fog_port)
        fog.start_server()