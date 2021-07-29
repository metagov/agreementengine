class AgreementProcess:
    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return self.__class__.__name__

    def create(self): ...
    
    def receive(self, data): ...

    def destroy(self): ...
