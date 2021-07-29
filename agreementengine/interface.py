class Interface:
    def __init__(self, request):
        self.request = request
        self.name = self.__class__.__name__

    def filter(self):
        return True

    def parse(self):
        return self.request.json

    def match(self):
        """
        Example database query match:

        QueryAgreement = Query()
        QueryInterface = Query()

        query = QueryAgreement.interfaces.any(
            (QueryInterface.type == self.name) &
            (QueryInterface.id == request.json['id'])
        )
        
        return query

        Example new agreement match:

        return self.new_agreement()
        """
        print('The default interface matches no agreements by default, please override the match() function.')
        return None
    
    def new_agreement(self):
        return {}
