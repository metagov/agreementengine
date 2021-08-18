import sys

sys.path.append('..\..\..')

from agreementengine.server import Server
import agreementpath

app = Server('db.json')
app.add_path(agreementpath.ScarceKnowledge)
app.run()