import sys

sys.path.append('../agreementengine')

from agreementengine import AgreementPath, AgreementProcess
from agreementengine.server import Server
from agreementengine.interface import Interface
from tinydb import Query

class TestInterface(Interface):
    def filter(request):
        return request.host_url == 'http://127.0.0.1:5000/'

    def parse(request):
        pass

    def match():
        Twitter = Query()
        queries = [
            Twitter.thread_id == '3849',
            Twitter.user_id == 'lukvmil'
        ]

        

class ExampleAgreement(AgreementPath):
    class Authoring(AgreementProcess):
        interfaces = [TestInterface]
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