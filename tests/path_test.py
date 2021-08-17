import sys

sys.path.append('../agreementengine')

from agreementengine import AgreementPath, AgreementProcess
from agreementengine.interface import Interface, DummyInterface

class NDA(AgreementPath):
    class Authoring(AgreementProcess):
        def create(self):
            print('Initializing Authoring state')

        def check(self):
            self.path.transition_to(NDA.Registration)
        
        def destroy(self):
            print('Destructing Authoring state')

    class Registration(AgreementProcess):
        def create(self):
            print('Initializing Registration state')
            self.funds_raised = 0


        def check(self):
            self.path.terminate()
        
        def destroy(self):
            print('Destructing Registration state')

    init = Authoring
    interfaces = [
        Interface,
        DummyInterface
    ]