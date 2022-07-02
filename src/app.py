from flask import Flask, redirect, request, url_for
from flask_marshmallow import Marshmallow
from src.helpers import calculate_bookkeeping
from src.jsons_schema import JsonSchema

app = Flask(__name__)
ma = Marshmallow(app)


@app.route("/")
def index():
    return redirect(url_for("generate_bookkiping"))


@app.route("/bookkipping", methods=["GET", "POST"])
def generate_bookkiping():
    if request.method != "POST":
        return "Moi! Don't forget to make a POST request to the /bookipping route!"

    payload = request.get_json(force=True)
    if errors := JsonSchema().validate(payload):
        return errors, 422
    return calculate_bookkeeping(payload)


if __name__ == "__main__":
    app.run()
