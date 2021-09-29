from agreementengine.interface import Interface
from tinydb import Query

class TwitterInterface(Interface):
    def filter(self):
        return True

    def match(self):
        text = self.request.json['full_text'][len('@agreementengine '):]
        
        if 'agreement' in text:
            return {
                'id': self.request.json['id_str']
            }

        elif 'broken' in text:
            print(self.request.json['in_reply_to_status_id_str'])
            return Query()['agreement']['TwitterInterface']['id'] == self.request.json['in_reply_to_status_id_str']
            
        elif 'upheld' in text:
            return Query()['agreement'][self.name]['id'] == self.request.json['in_reply_to_status_id_str']
