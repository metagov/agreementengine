import sys

sys.path.append('..\..\..')

from agreementengine import AgreementPath, AgreementProcess
from interfaces import *

class GhostKnowledge(AgreementPath):

    class Authoring(AgreementProcess):
        def first(self):
            self.path.model.set('process', 'Authoring')
            print('i now exist')
        
        def on_receive(self, data):
            if data['type'] == 'new_request':
                self.model.add_record(data)
                self.model.set('total', int(data['contribution']))
            elif data['type'] == 'new_pledge':
                self.model.add_record(data)
                total = self.model.get('total')
                self.model.set('total', total + int(data['contribution']))

            if self.model.get('total') > 500:
                self.path.transition_to(GhostKnowledge.Registration)
        
        def last(self):
            print('i am now dead')
            # ServerInterface.report_id(self.model.id)
    
    class Registration(AgreementProcess):
        def create(self):
            self.path.model.set('process', 'Registration')
    
    interfaces = [
        ServerInterface
    ]

    default_model = {
        "total_contributions": 0
    }

    init = Authoring
    