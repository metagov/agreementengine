import sys

sys.path.append('..\..\..')

from agreementengine import AgreementPath, AgreementProcess
from interfaces import *

class TSC(AgreementPath):

    class Authoring(AgreementProcess):
        def on_receive(self, data):
            self.model.set('data', 'creator_id', data['user']['id_str'])
            try:
                self.model.set('data', 'member_id', data['entities']['user_mentions'][1]['id_str'])
            except IndexError:
                print('Agreement missing other user')
                self.path.terminate()
                return

            self.path.transition_to(TSC.Registration)

    class Registration(AgreementProcess):
        def on_receive(self, data):
            ...
    
    interfaces = [
        TwitterInterface
    ]

    init = Authoring
