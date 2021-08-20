import sys

sys.path.append('..\..\..')

from agreementengine import AgreementPath, AgreementProcess
from interfaces import *

class TSC(AgreementPath):

    class Authoring(AgreementProcess):
        def on_receive(self, data):
            print(data)
    
    interfaces = [
        TwitterInterface
    ]

    init = Authoring
