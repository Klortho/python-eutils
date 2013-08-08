# http wrapper for backend calls

import requests

class cgi(object):
    def __init__(self, url):
        self.url = url
        
    def post(self, path = '', data = {}):
        return requests.post(self.url + path, data=data)
    
    def get(self, path = '', data = {}):
        return requests.get(self.url + path, params=data)    
