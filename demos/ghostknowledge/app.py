from flask import Flask, render_template, request

app = Flask('GhostKnowledge')

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        print(request.form)
    return render_template("home.html")



app.run(debug=True)