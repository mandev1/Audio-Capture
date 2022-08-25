from flask import Flask, request, redirect, render_template
from datetime import datetime

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def homepage():
    today = datetime.now()
    today = today.strftime("%d/%m/%Y   %H:%M:%S")
    text = request.form["Mytext"]
    texting = today+ "\t" + text + "\n"
    print(texting)
    return texting


if __name__ == "__main__":
    app.run(debug=True, port=3000)
