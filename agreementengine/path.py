from .interface import Interface
from .model import AgreementModel
from tinydb.queries import QueryInstance
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
            # Creating interface object
            interface = Interface(request)
            if interface.filter():
                
                match = interface.match()

                if type(match) == QueryInstance:
                    docs = cls.db.search(match)
                    num_docs = len(docs)
                    
                    # Ideal scenario, one agreement matched
                    if num_docs == 1:
                        # doc_id = docs[0].doc_id
                        # agreement = cls.recall(doc_id)
                        pass
                    
                    # Too many agreements matched
                    elif num_docs > 1:
                        pass
                    
                    # No agreements matched, use other return type to make a new agreement
                    elif num_docs == 0:
                        pass

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