from flask import Flask, render_template, request
from tinydb import TinyDB
import requests

app = Flask('GhostKnowledge')
ae_url = "http://127.0.0.1:5000/GhostKnowledge"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/new_request", methods=["POST", "GET"])
def new_request():
    if request.method == "POST":
        form = dict(request.form)
        print(form)
        try:
            requests.post(url=ae_url, json=form)
        except requests.exceptions.ConnectionError:
            print('Failed to send form')
    return render_template("new_request.html")

@app.route("/new_pledge", methods=["POST", "GET"])
def new_pledge():
    if request.method == "POST":
        form = dict(request.form)
        print(form)
        try:
            requests.post(url=ae_url, json=form)
        except requests.exceptions.ConnectionError:
            print('Failed to send form')

    data = requests.get(url=ae_url).json()

    agreements = []

    for id, data in data['agreements'].items():
        if 'content' in data:
            agreements.append({
                'id': id,
                'content': data['content']
            })

    return render_template("new_pledge.html", agreements=agreements)

@app.route("/accept_request/<id>", methods=["POST", "GET"])
def accept_request(id):
    if request.method == "POST":
        form = dict(request.form)
        print(form)
        try:
            requests.post(url=ae_url, json=form)
        except requests.exceptions.ConnectionError:
            print('Failed to send form')
    
    data = requests.get(url=ae_url).json()
    agreement = data['agreements'][id]

    return render_template("accept_request.html", agreement=agreement)

@app.route("/submit_essay/<id>", methods=["POST", "GET"])
def submit_essay(id):
    if request.method == "POST":
        form = dict(request.form)
        form['id'] = id
        print(form)
        try:
            requests.post(url=ae_url, json=form)
        except requests.exceptions.ConnectionError:
            print('Failed to send form')
    
    return render_template("submit_essay.html")

app.run(host='0.0.0.0', port=4999)