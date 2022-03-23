from flask import Flask

class PyHTML:
    def div(self, classes:list=[], ids:list=[], styles:list=[]):
        pass

class NextPy:
    def __init__(self):
        self.app = Flask(__name__)
        self.endpoints = []
        
    def add_endpoint(self, endpoint, handler):
        self.endpoints.append(endpoint)
        self.app.add_url_rule(endpoint.url, endpoint.name, handler)
        
    def run(self, host = "localhost", port = 5000):
        self.app.run(host = host, port = port)