from flask import Flask, request, Response
from tinydb import TinyDB
import json

class Server:
    def __init__(self, db_fn):
        self.flask_app = Flask(__name__)
        self.db = TinyDB(db_fn, indent=2)

    def add_path(self, Path):
        print('Added route for', Path.__name__)
        # Adding new listener route for the Path
        @self.flask_app.route(f'/{Path.__name__}', methods=['POST', 'GET'])
        def respond():
            if request.method == 'POST':
                if Path.route(request):
                    return Response(status=200)
                else:
                    # not sure if this is the right response code?
                    # This response is given if the agreement path has no interface to handle the request
                    return Response(status=406)
            
            elif request.method == 'GET':
                agreements = Path.db.all()
                package = {
                    "count": len(agreements),
                    "agreements": {}
                }
                for a in agreements:
                    package["agreements"][str(a.doc_id)] = a['public']
                
                return package

        # Adding database table for new Agreement Path
        Path.db = self.db.table(Path.__name__)
    
    def run(self):
        self.flask_app.run()
