from prototype4 import AgreementState, AgreementPath
import metagov.twitter
from agreementengine import agreement

class Registration(agreement.State):
    name = "Registration"
    def __init__(self, path) -> None:
        super().__init__()

class Authoring(agreement.State):
    def __init__(self, path) -> None:
        super().__init__()

    def listen(self):
        resp = metagov.twitter.listenfor("agreement")

        

        if resp['username'] == '@vbuterin':
            self.path.to(Registration)
