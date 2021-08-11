import sys

sys.path.append('..\..\..')

from agreementengine import AgreementPath, AgreementProcess
from interfaces import *
import requests
import random

class GhostKnowledge(AgreementPath):

    class Authoring(AgreementProcess):
        def on_receive(self, data):
            if data['type'] == 'new_request':
                self.model.set('data', 'total_contributions', int(data['contribution']))
                
                self.model.set('public', 'content', data['content'])
                self.model.set('public', 'author', data['author'])
                self.model.set('public', 'total_contributions', self.model.get('data', 'total_contributions'))
                self.model.set('public', 'id', self.model.doc_id)
                
            elif data['type'] == 'new_pledge':
                self.model.update('data', 'total_contributions', lambda x: x + int(data['contribution']))
                self.model.set('public', 'total_contributions', self.model.get('data', 'total_contributions'))

            if self.model.get('data', 'total_contributions') > 500:
                self.path.transition_to(GhostKnowledge.Registration)
    
    class Registration(AgreementProcess):
        def first(self):
            security_code = str(random.randint(0, 1000000))
            self.model.set('data', 'security_code', security_code)
            author = self.model.get('public', 'author')[1:]
            
            message = f"You've been invited to write an essay for Ghost Knowledge! View your request here: http://127.0.0.1:4999/accept_request/{self.model.doc_id} and use the security code: {security_code}"
            mg = MetagovInterface(self.model.get('data', 'metagov_url'), self.model.get('data', 'metagov_slug'))

            user_id = mg.do('twitter.get-user-id', {'screen_name': author}).json()
            if user_id:
                mg.do('twitter.send-dm', {'user_id': str(user_id), 'text': message})
            else:
                print('could not find user')

        
        def on_receive(self, data):
            if data['type'] == 'accept_request':
                if data['security_code'] == self.model.get('data', 'security_code'):
                    if data['accept'] == 'yes':
                        self.path.transition_to(GhostKnowledge.Maintenance)

                    elif data['accept'] == 'no':
                        self.path.terminate()


    class Maintenance(AgreementProcess):
        def first(self):
            print('starting maintenance')

    
    interfaces = [
        ServerInterface
    ]

    default_model = {
        "total_contributions": 0,
        "metagov_url": "http://127.0.0.1:8000",
        "metagov_slug": "a9fa02a7-de85-47ba-8bc0-bac507b50150"
    }

    init = Authoring
    