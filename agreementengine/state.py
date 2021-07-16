class AgreementState:
    def __init__(self, path):
        self.path = path
        self.create()

    def __repr__(self):
        return self.__class__.__name__

    def create(self):
        pass

    def destroy(self):
        pass

    def receive(self):
        pass

    def transmit(self):
        pass