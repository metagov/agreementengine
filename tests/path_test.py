import sys

sys.path.append('../agreementengine')

from agreementengine import AgreementPath, AgreementState
from agreementengine.interfaces import *
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
            self.funds_raised = 0
            self.interface.connect(PayPal)
        
        def check(self):
            if self.funds_raised >= 500:
                self.interface.emit(Slack, "Funding reached!")
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
    interfaces = (
        PayPal,
        MailGun,

    )

nda_contract = NDA()
nda_contract.start()
while nda_contract.alive:
    nda_contract.tick()