import sys

sys.path.append('..\..\..')

from agreementengine.interface import Interface
from tinydb import Query
import requests

class ServerInterface(Interface):
    def filter(self):
        return self.request.remote_addr == '127.0.0.1'
    
    def match(self):
        data = self.request.json 
        
        if data['type'] == 'new_request':
            return {}

        if data['type'] == 'new_pledge':
            return int(self.request.json['agreement'])
    
    def report_id(_id):
        payload = {
            'agreement_id': _id
        }
        requests.post(url='http://127.0.0.1:4999/', data=payload)