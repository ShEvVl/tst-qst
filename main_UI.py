import random

import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/request")
def Request():
    return render_template(
        "Request.html",
        data=[{'name': x} for x in req]
    )


@app.route("/response", methods=["GET", "POST"])
def Response():
    select_all = [request.form.get(f"comp_select{x}") for x in range(1, 11)]
    select = []
    for i in select_all:
        if i != None:
            select.append(i)
        else:
            pass
    return render_template(
        "Response.html",
        data=[
            {"output": output(select)[0], "input": select, "count": output(select)[2]}
        ],
    )


@app.route("/data")
def get_table():
    return render_template(
        "Data.html", tables=[df.to_html(classes="data")], titles=df.columns.values
    )


with open("info.csv", "r") as f:
    source = f.readlines()

data = []
for i in range(len(source)):
    data.append(source[i].replace("\n", ""))
df = pd.Series(data).str.split(pat=";", expand=True)
df.columns = ["Path", "amount_of_shows"]+[f"category{x}" for x in range(1, 11)]
df["amount_of_shows"] = df["amount_of_shows"].astype(int)

req = list(set(df.iloc[:, 2:].values.flatten()))
log_ind = []


def output(r):
    seq = []
    if r == []:
        top_seq_path = df.iloc[random.randint(0, len(df) - 1), 0]
        ind_top = df.index[df["Path"] == top_seq_path].tolist()
        log_ind.append(ind_top[0])
    else:
        for i in range(len(r)):
            for k in range(10):
                c = df.index[df[f"category{k + 1}"] == r[i]].tolist()
                if c == []:
                    pass
                else:
                    seq.append(c)
        seq_u = list(set([item for sublist in seq for item in sublist]))
        df_t = df.iloc[seq_u].sort_values(by=["amount_of_shows"], ascending=False)
        top_seq_path = df_t.iloc[0, 0]
        ind_top = df.index[df["Path"] == top_seq_path].tolist()
        if log_ind == []:
            pass
        else:
            if ind_top[0] == log_ind[-1]:
                rand_ind = random.randint(0, len(df_t) - 1)
                while log_ind[-1] == rand_ind:
                    rand_ind = random.randint(0, len(df_t) - 1)
                else:
                    top_seq_path = df_t.iloc[rand_ind, 0]
                    ind_top = df.index[df["Path"] == top_seq_path].tolist()
        log_ind.append(ind_top[0])
        df.iloc[ind_top, 1] = df.iloc[ind_top, 1] - 1
        if df.iloc[ind_top, 1].values[0] > 0:
            pass
        else:
            top_seq_path = ""
    return top_seq_path, log_ind, df.iloc[ind_top, 1].values[0]


if __name__ == "__main__":
    app.run(debug=True, port=8080)
