from flask import Flask, render_template, request
from utils import output, req, df


app = Flask(__name__)


@app.route("/")
@app.route("/request")
def get_request():
    return render_template(
        "request.html",
        data=[{'name': x} for x in req]
    )


@app.route("/response", methods=["GET", "POST"])
def get_response():
    select_all = [request.form.get(f"comp_select{x}") for x in range(1, 11)]
    select = []
    for i in select_all:
        if i is not None:
            select.append(i)
        else:
            pass
    return render_template(
        "response.html",
        data=[
            {"output": output(select)[0], "input": select, "count": output(select)[2]}
        ]
    )


@app.route("/data")
def get_table():
    return render_template(
        "data.html", tables=[df.to_html(classes="data")], titles=df.columns.values
    )


if __name__ == "__main__":
    app.run(debug=True, port=8080)
