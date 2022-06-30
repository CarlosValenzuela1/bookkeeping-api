from flask import Flask, redirect, url_for, request
from src.helpers import get_bookkipping

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for("generate_bookkiping"))


@app.route("/bookkipping", methods=["GET", "POST"])
def generate_bookkiping():
    if request.method != "POST":
        return "Moi! Don't forget to make a POST request to the /bookipping route!"

    payload = request.get_json(force=True)
    return get_bookkipping(payload)


if __name__ == "__main__":
    app.run()
