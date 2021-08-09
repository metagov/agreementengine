class AgreementProcess:
    def __init__(self, path):
        self.path = path
        self.model = path.model
        self.name = self.__class__.__name__

    # Backend functions
    def _create(self):
        self.model.set('process', self.name)
        self.first()

    def _send(self, data):
        self.on_receive(data)

    def _destroy(self):
        self.last()

    # User overriden functions
    def first(self): ...
    
    def on_receive(self, data): ...

    def last(self): ...
