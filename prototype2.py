import enum

class AgreementStates(enum.Enum):
    REGISTRATION = 1
    AUTHENTICATION = 2
    MAINTENANCE = 3
    RESOLUTION = 4
    TERMINATION = 5



class Agreement:
    def __init__(self):
        self.state = AgreementStates.REGISTRATION

nda = Agreement()

class AgreementPath():
    def __init__(self):
        self.model = ""

    def register(self):
        pass

    def authenticate(self):
        pass

    def maintain(self):
        pass

    def resolve(self):
        pass

    def terminate(self):
        pass
    