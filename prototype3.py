from agreementengine.paths import State

State.REGISTRATION

class Registration:
    def __init__(self, path):
        self.container.make_record

class AgreementEngine:
    def __init__(self):
        self.states = [
            Registration(self)
        ]
        self.state = 3

    def __getitem__(self, t):
        return self.states[t]
    
    def filter(self):
        self.states[self.state].filter()

ae = AgreementEngine()
ae.transition()