import sys

sys.path.append('..\..\..')

from agreementengine.interface import Interface
from tinydb import Query
import requests

class ServerInterface(Interface):
    def filter(request):
        print(request.host_url)
        print(request.url)
        return request.remote_addr == '127.0.0.1'
    
    def match(request):
        data = request.json 
        
        if data['type'] == 'new_request':
            return Interface.NEW_AGREEMENT

        if data['type'] == 'new_pledge':
            return [
                Query().id == data['id']
            ]
    
    def report_id(_id):
        payload = {
            'agreement_id': _id
        }
        requests.post(url='http://127.0.0.1:4999/', data=payload)