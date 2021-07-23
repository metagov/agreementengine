import sys

sys.path.append('../agreementengine')

from agreementengine import AgreementPath, AgreementProcess
from agreementengine.server import Server
from agreementengine.interface import Interface


class TestInterface(Interface):
    @classmethod
    def filter(cls, request):
        print(request.data)

class ExampleAgreement(AgreementPath):
    class Authoring(AgreementProcess):
        def check(self):
            self.path.transition_to(ExampleAgreement.End)
    
    class End(AgreementProcess):
        def check(self):
            self.path.terminate()

    interfaces = [
        TestInterface
    ]



server = Server('db.json')
server.add_path(ExampleAgreement)
server.run()