import dataset

class AgreementModel:
    def __init__(self):
        self.db_fn = 'agreements.db'
        self.db = dataset.connect(f'sqlite:///{self.db_fn}')