from flask import Flask, redirect, url_for, request
from src.helpers import get_bookkipping

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for("generate_bookkiping"))


@app.route("/bookkipping", methods=["GET", "POST"])
def generate_bookkiping():
    result = get_bookkipping()
    return result


if __name__ == "__main__":
    app.run()
