import enum

class State(enum.Enum):
    AUTHORING = 1
    REGISTRATION = 2
    MAINTENANCE = 3
    RESOLUTION = 4
    ENFORCEMENT = 5

class AgreementState:
    def __init__(self, path):
        self.path = path

    def record(self, data):
        self.path.add_record(
            self.__class__.__name__, 
            data)

    def initialize(self):
        pass

    def check(self):
        pass
    
    def destruct(self):
        pass

class AgreementModel:
    def __init__(self):
        pass

class AgreementPath:
    def __init__(self):
        self.state = None
        self.model = AgreementModel(self)

    def transition_to(self, NewState):
        self.state.destruct()
        self.state = NewState(self)


