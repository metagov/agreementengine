import datetime

class AgreementModel:
    def __init__(self, db, doc_id=None, init=None):
        """
        Supports two methods of initialization:
        Setting the doc_id parameter will load an existing agreement entry with the inputted id
        Setting the init parameter will create a new agreement entry initialized with the inputted data
        """

        self.db = db

        default_model = {
            "agreement": {},
            "data": {},
            "public": {},
            "record": []
        }

        if doc_id is not None:
            self.doc_id = doc_id

            if not db.get(doc_id=doc_id):
                raise KeyError('doc_id is not in use')
            
            if init is not None:
                print('Model loaded from doc_id, ignoring init data')
        
        else:
            model = default_model.copy()

            if init is not None:
                if type(init) == dict:
                    model['data'] = init
                else:
                    raise TypeError("init parameter must be of type 'dict'")

            self.doc_id = db.insert(model)

    def get(self, field, key):
        return self.db.get(doc_id=self.doc_id)[field][key]
    
    def set(self, field, key, val):
        self.db.update(lambda d: d[field].update({key: val}), doc_ids=[self.doc_id])
    
    def update(self, field, key, func):
        self.set(field, key, func(self.get(field, key)))

    def add_record(self, data):
        new_record = {
            'timestamp': str(datetime.datetime.now()),
            'data': data
        }

        self.db.update(
            lambda doc : doc['record'].append(new_record),
            doc_ids = [self.doc_id]
        )