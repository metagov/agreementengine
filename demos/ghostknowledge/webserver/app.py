from flask import Flask, render_template, request
import requests

app = Flask('GhostKnowledge')

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        form = dict(request.form)
        print(form)
        try:
            requests.post(url="http://127.0.0.1:5000/GhostKnowledge", json=form)
        except requests.exceptions.ConnectionError:
            print('Failed to send form')
    return render_template("home.html")



app.run(port=4999)