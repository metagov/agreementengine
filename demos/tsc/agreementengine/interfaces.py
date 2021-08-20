from agreementengine.interface import Interface

class TwitterInterface(Interface):
    def filter(self):
        return True

    def match(self):
        text = self.request.json['data']['full_text']
        
        return {}