from interface import Interface
from .model import AgreementModel
from tinydb import Query
from functools import reduce
import operator

class AgreementPath:
    interfaces = []
    db = None

    def __init__(self):
        self.name = self.__class__.__name__
        self.state = None
        self.alive = True
        self.model = AgreementModel(self.db)

    @classmethod
    def create(cls):
        agr = cls()
        return agr

    @classmethod
    def recall(cls, _id):
        agr = cls()
        return agr

    @classmethod
    def route(cls, request):
        for Interface in cls.interfaces:
            if Interface.filter(request):

                QueryAgreement = Query()
                QueryInterface = Query()

                documents = cls.db.search(
                    QueryAgreement.interfaces.any(
                        # Data must match the Interface being used
                        (QueryInterface.type == Interface.__name__) &
                        # Applying all queries written in Interface.match() 
                        reduce(operator.and_, Interface.match(request))
                    )
                )

                if len(documents) == 1: # matched one
                    document = documents[0]
                    doc_id = document.doc_id

                    data = Interface.parse(request)

                    agreement = cls.recall(doc_id)
                    agreement.send(data)

                elif len(documents) > 1: # matched many
                    return False

                else: # matched none
                    cls.create()

                return True
        return False
        
    def start(self):
        self.state = self.init(self)
    
    def tick(self):
        self.state.check()

    def transition_to(self, NextState):
        self.state.destroy()
        self.state = NextState(self)
    
    def terminate(self):
        self.state.destroy()
        self.alive = False