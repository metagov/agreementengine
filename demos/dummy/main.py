import sys

from flask.wrappers import Response

sys.path.append('..\..')

from agreementengine import AgreementPath, AgreementProcess
from agreementengine.interface import Interface
from agreementengine.server import Server
import external_processes

class DummyInterface(Interface):
    def filter(self):
        return True
    
    def match(self):
        return {}


class Dummy(AgreementPath):

    class Authoring(AgreementProcess):
        def on_receive(self, data):
            print("authoring")
            self.path.transition_to(Dummy.ImportedProcess)
    
    class Registration(AgreementProcess):
        def first(self):
            print('registration')
            self.path.transition_to(Dummy.Maintenance)

    class Maintenance(AgreementProcess):
        def first(self):
            print('maintenance')
            self.path.terminate()
    
    ImportedProcess = external_processes.TestProcess.transplant([Maintenance])
    
    interfaces = [DummyInterface]
    init = Authoring

app = Server('db.json')
app.add_path(Dummy)
app.run()