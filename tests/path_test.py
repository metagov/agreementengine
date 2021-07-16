import sys

sys.path.append('../agreementengine')

from agreementengine import AgreementPath, AgreementState
from tinydb import TinyDB

class NDA(AgreementPath):
    class Authoring(AgreementState):
        def create(self):
            print('Initializing Authoring state')
        
        def check(self):
            self.path.transition_to(NDA.Registration)
        
        def destroy(self):
            print('Destructing Authoring state')

    class Registration(AgreementState):
        def create(self):
            print('Initializing Registration state')
        
        def check(self):
            self.path.transition_to(NDA.Maintenance)
        
        def destroy(self):
            print('Destructing Registration state')
    
    class Maintenance(AgreementState):
        def create(self):
            print('Initializing Maintenance state')
        
        def check(self):
            self.path.transition_to(NDA.Resolution)

        def destroy(self):
            print('Destructing Maintenance state')

    class Resolution(AgreementState):
        def create(self):
            print('Initializing Resolution state')
        
        def check(self):
            self.path.terminate()

        def destroy(self):
            print('Destructing Resolution state')

    init = Authoring

nda_contract = NDA()
nda_contract.start()
while nda_contract.alive:
    nda_contract.tick()