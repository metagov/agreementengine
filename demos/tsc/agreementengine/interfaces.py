from agreementengine.interface import Interface
from tinydb import Query
import tweepy, json

class TwitterInterface(Interface):
    def filter(self):
        return True

    def match(self):
        self.parsed_text = self.request.json['full_text'][len('@agreementengine '):]
        
        if 'agreement' in self.parsed_text:
            return {
                'id': self.request.json['id_str']
            }

        else:
            # matches to agreement being replied to
            return Query()['agreement']['TwitterInterface']['id'] == self.request.json['in_reply_to_status_id_str']

    def parse(self):
        parsed_data = self.request.json

        if 'broken' in self.parsed_text:
            parsed_data['type'] = 'broken'
        elif 'upheld' in self.parsed_text:
            parsed_data['type'] = 'upheld'
        else:
            parsed_data['type'] = None

        return parsed_data

def tweet(status, in_reply_to):
    with open('../twitter/apikeys.json', 'r') as f:
        keys = json.load(f)

    # sending keys to authenticator
    auth = tweepy.OAuthHandler(
        keys['API key'], 
        keys['API key secret'])

    auth.set_access_token(
        keys['Access token'], 
        keys['Acess token secret'])

    api = tweepy.API(auth)
    api.update_status(status, in_reply_to, auto_populate_reply_metadata=True)