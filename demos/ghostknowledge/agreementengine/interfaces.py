import sys

sys.path.append('..\..\..')

from agreementengine.interface import Interface
import requests

class ServerInterface(Interface):
    def filter(self):
        return self.request.remote_addr == '127.0.0.1'
    
    def match(self):
        data = self.request.json

        print(data)
        
        if data['type'] == 'new_request':
            return {}

        elif data['type'] == 'new_pledge':
            return int(self.request.json['agreement'])
        
        elif data['type'] == 'accept_request':
            return int(self.request.json['id'])

        elif data['type'] == 'submit_essay':
            return int(self.request.json['id'])


class MetagovInterface:
    def __init__(self, url, slug):
        self.url = url
        self.slug = slug
    
    def do(self, action, params):
        resp = requests.post(
            url = self.url + '/api/internal/action/' + action,
            headers = {'Content-Type': 'application/json', 'X-Metagov-Community': self.slug},
            json = {'parameters': params}
        )
        return resp