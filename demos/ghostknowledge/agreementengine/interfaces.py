import sys

sys.path.append('..\..\..')

from agreementengine.interface import Interface

class ServerInterface(Interface):
    def filter(self):
        return self.request.remote_addr == '127.0.0.1'
    
    def match(self):
        data = self.request.json 
        
        if data['type'] == 'new_request':
            return {}

        if data['type'] == 'new_pledge':
            return int(self.request.json['agreement'])