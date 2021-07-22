from flask import Flask, request, Response
import json

class Listener:
    def __init__(self):
        self.flask_app = Flask(__name__)

    def add_path(self, Path):
        print('Added listener for', Path.__name__)
        # Adding new listener route for the Path
        @self.flask_app.route(f'/{Path.__name__}', methods=['POST'])
        def respond():
            Path.filter(request)
            return Response(status=200)
    
    def run(self):
        self.flask_app.run()
