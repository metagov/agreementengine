from agreementengine import agreements

class NDA(ae.AgreementPath):
    def __init__(self) -> None:
        super().__init__()

    
class NDA(agreements.Path):
    class Registration(agreements.State):
        def init(self):
            pass

        def destroy(self):
            pass
    
    class 
