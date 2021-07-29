class AgreementModel:
    def __init__(self, db, doc_id=None, init=None):
        if doc_id and init:
            raise TypeError('AgreementModel takes either a doc_id or init parameter, not both')

        if doc_id:
            self.doc_id = doc_id
            if not db.get(doc_id=doc_id):
                raise KeyError('doc_id is not in use')
        
        if init:
            self.doc_id = db.insert(init)

    def get(self, key):
        return self.entry[key]
        pass

    def set(self, key, val):
        db.update({key: val}, self.doc_id)

