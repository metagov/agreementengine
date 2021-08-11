from .interface import Interface
from .model import AgreementModel
from .exceptions import *
from tinydb.queries import QueryInstance

class AgreementPath:
    interfaces = []
    db = None
    default_model = {}

    def __init__(self, model, process=None):
        self.name = self.__class__.__name__
        self.alive = True
        self.process = process
        self.model = model

    @classmethod
    def create(cls):
        agr = cls(AgreementModel(cls.db, init=cls.default_model))
        agr.start()
        return agr

    @classmethod
    def recall(cls, doc_id):
        agr = cls(AgreementModel(cls.db, doc_id=doc_id))
        process_name = agr.model.get('agreement', 'process')
        Process = cls.__dict__[process_name]
        agr.process = Process(agr)
        return agr

    @classmethod
    def route(cls, request):
        for Interface in cls.interfaces:
            # Creating interface object
            interface = Interface(request)
            if interface.filter():
                
                match = interface.match()

                if type(match) == int:
                    doc_id = match
                    agreement = cls.recall(doc_id)

                elif type(match) == QueryInstance:
                    docs = cls.db.search(match)
                    num_docs = len(docs)
                    
                    # Ideal scenario, one agreement matched
                    if num_docs == 1:
                        doc_id = docs[0].doc_id
                        agreement = cls.recall(doc_id)
                    
                    # Too many agreements matched
                    elif num_docs > 1:
                        pass
                    
                    # No agreements matched, use other return type to make a new agreement
                    elif num_docs == 0:
                        pass
                
                elif type(match) == dict:
                    agreement = cls.create()
                    agreement.model.set('agreement', interface.name, match)

                else:
                    raise TypeError('Interface.match() must return a QueryInstance or a Dictionary')

                agreement.process._send(interface.parse())
                return True
        return False
        
    def start(self):
        self.process = self.init(self)
        self.process._create()

    def transition_to(self, NextState):
        self.process._destroy()
        self.process = NextState(self)
        self.process._create()
    
    def terminate(self):
        self.process._destroy()
        self.alive = False