class AgreementModel:
    def __init__(self, db, doc_id=None, init=None):
        self.db = db

        if doc_id and (init is not None):
            raise TypeError('AgreementModel takes either a doc_id or init parameter, not both')

        if doc_id:
            self.doc_id = doc_id
            if not db.get(doc_id=doc_id):
                raise KeyError('doc_id is not in use')
        
        if init is not None:
            self.doc_id = db.insert(init)

    def get(self, key):
        return self.db.get(doc_id=self.doc_id)[key]

    def set(self, key, val):
        self.db.update({key: val}, doc_ids=[self.doc_id])
