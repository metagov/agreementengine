from .model import AgreementModel

class AgreementPath:
    def __init__(self):
        self.state = None
        self.model = AgreementModel()
        
    def start(self):
        self.state = self.init(self)
    
    def transition_to(self, NextState):
        self.state.destroy()
        self.state = NextState(self)
    
