class AgreementProcess:
    def __init__(self, path):
        self.path = path
        self.create()

    def __repr__(self):
        return self.__class__.__name__

    def create(self): ...
    
    def receive(self, payload): ...

    def destroy(self): ...
