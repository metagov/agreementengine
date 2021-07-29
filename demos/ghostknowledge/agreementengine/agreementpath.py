import sys

sys.path.append('..\..\..')

from agreementengine import AgreementPath, AgreementProcess
from interfaces import *

class GhostKnowledge(AgreementPath):

    class Authoring(AgreementProcess):
        def create(self):
            print('i now exist')
        
        def on_receive(self, data):
            self.path.model.set('content', data)
            self.path.terminate()
        
        def destroy(self):
            print('i am now dead')
            # ServerInterface.report_id(self.model.id)
    
    interfaces = [
        ServerInterface
    ]

    init = Authoring
    