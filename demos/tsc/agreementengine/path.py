import sys

from requests.models import parse_header_links

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

            self.model.set('data', 'member_voted', False)
            self.model.set('data', 'creator_voted', False)

            self.path.transition_to(TSC.Maintenance)

    class Maintenance(AgreementProcess):
        def on_receive(self, data):
            if data['user']['id_str'] == self.model.get('data', 'creator_id'):
                self.model.set('data', 'creator_ruling', data['type'])
                self.model.set('data', 'creator_voted', True)
            elif data['user']['id_str'] == self.model.get('data', 'member_id'):
                self.model.set('data', 'member_ruling', data['type'])
                self.model.set('data', 'member_voted', True)
            
            if (self.model.get('data', 'member_voted')) and (self.model.get('data', 'creator_voted')):

                member_ruling = self.model.get('data', 'member_ruling')
                creator_ruling = self.model.get('data', 'creator_ruling')

                if (member_ruling == creator_ruling):
                    self.model.set('data', 'outcome', member_ruling)
                    self.path.transition_to(TSC.Enforcement)
                else:
                    self.model.set('data', 'outcome', 'disputed')
                    self.path.transition_to(TSC.Resolution)
    
    class Resolution(AgreementProcess):
        def first(self):
            tweet(
                "The outcome of the agreement is disputed, one user must change their response in order to decide upon the outcome.",
                self.model.get('agreement', 'TwitterInterface')['id']
            )

            self.path.transition_to(TSC.Maintenance)

    class Enforcement(AgreementProcess):
        def first(self):
            type = self.model.get('data', 'outcome')
            msg = None
            if type == 'upheld':
                msg = 'The agreement has been upheld by the creator!'
            elif type == 'broken':
                msg = 'The agreement has been broken by the creator.'
            
            if msg: tweet(msg, self.model.get('agreement', 'TwitterInterface')['id'])
            self.path.terminate()

    interfaces = [
        TwitterInterface
    ]

    init = Authoring
