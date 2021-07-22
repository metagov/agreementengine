import sys

sys.path.append('../agreementengine')

from agreementengine import AgreementPath, AgreementProcess
from tinydb import TinyDB

class Authoring(AgreementProcess):
    def create(self):
        print('Initializing Authoring state')
    
    def check(self):
        
        self.path.transition_to(Registration)
    
    def destroy(self):
        print('Destructing Authoring state')

class Registration(AgreementProcess):
    def create(self):
        print('Initializing Registration state')
    
    def check(self):
        self.path.transition_to(Maintenance)
    
    def destroy(self):
        print('Destructing Registration state')

class Maintenance(AgreementProcess):
    def create(self):
        print('Initializing Maintenance state')
    
    def check(self):
        self.path.transition_to(Resolution)

    def destroy(self):
        print('Destructing Maintenance state')

class Resolution(AgreementProcess):
    def create(self):
        print('Initializing Resolution state')
    
    def check(self):
        self.path.terminate()

    def destroy(self):
        print('Destructing Resolution state')

class NDA(AgreementPath):
    init = Authoring

nda_contract = NDA()
nda_contract.start()
while nda_contract.alive:
    nda_contract.tick()