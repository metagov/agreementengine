import sys

sys.path.append('../agreementengine')

from agreementengine import AgreementPath, AgreementState
from tinydb import TinyDB

class NDA(AgreementPath):
    class Registration(AgreementState):
        def create(self):
            print('initializing')
        
        def check(self):
            self.path.transition_to(NDA.Registration)
            self.path.terminate()
    
    init = Registration

nda_contract = NDA()
nda_contract.start()