import sys

sys.path.append('../../..')

from agreementengine.server import Server
import path

app = Server('db.json')
app.add_path(path.TSC)
app.run()