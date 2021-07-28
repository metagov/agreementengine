import sys

sys.path.append('..\..\..')

from agreementengine import AgreementPath, AgreementProcess
from interfaces import *

class GhostKnowledge(AgreementPath):

    class Authoring(AgreementProcess):
        def first(self):
            print('i exist')
        
        def on_receive(self, payload):
            self.model.set_content(payload)
            self.path.transition_to()
        
        def last(self):
            ServerInterface.report_id(self.model.id)
    
    interfaces = [
        ServerInterface
    ]

    init = Authoring
    