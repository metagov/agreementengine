import sys

sys.path.append('../../..')

from agreementengine import AgreementProcess

class SwappableProcess(AgreementProcess):
    transitions = []

    @classmethod
    def transplant(cls, transitions):
        cls.transitions = transitions
        return cls

class TestProcess(SwappableProcess):
    def first(self):
        print('Initializing TestProcess')
        self.path.transition_to(self.transitions[0])
    
    def on_receive(self, data):
        print('Received data for TestProcess')
    
    def last(self):
        print('Destroying TestProcess')


class SwappableAuthoring(SwappableProcess):
    def on_receive(self, data):
        ...