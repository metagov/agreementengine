from flask import Flask, Response, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def home():
    print(request.json)
    print(request.host, request.host_url)
    print(request.remote_addr)
    return Response(status=200)

app.run(port=1000, debug=True)