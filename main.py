from flask import Flask, render_template, request
from utils import output

app = Flask(__name__)


@app.route("/")
def main():
    get_categories = request.args.getlist('category[]')
    if output(get_categories)[2] > 0:
        return render_template(
            "index.html", data=output(get_categories)[0]
            )
    else:
        return ("", 204)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
