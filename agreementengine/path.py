from .model import AgreementModel

class AgreementPath:
    interfaces = []
    db = None
    
    def __init__(self):
        self.name = self.__class__.__name__
        self.state = None
        self.alive = True
        self.model = AgreementModel()

        self.setup()

    @classmethod
    def route(cls, request):
        for Interface in cls.interfaces:
            if Interface.filter(request):
                # Interface.
                pass
                return True

        return False

    @staticmethod
    def get_agreement(aeid):
        pass


    def setup(self):
        pass
        
    def start(self):
        self.state = self.init(self)
    
    def tick(self):
        self.state.check()

    def transition_to(self, NextState):
        self.state.destroy()
        self.state = NextState(self)
    
    def terminate(self):
        self.state.destroy()
        self.alive = False