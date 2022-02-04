from flask import Flask, render_template, request
from utils import output

app = Flask(__name__)


@app.route("/")
def main():
    cats = request.args.getlist('category[]')
    return render_template(
        "index.html", data=output(cats)[0]
    )


if __name__ == "__main__":
    app.run(debug=True, port=8080)
