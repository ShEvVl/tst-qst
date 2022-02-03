import random

import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/request')
def Request():
    return render_template(
        'Request.html',
        data=[{'name': req[0]},
              {'name': req[1]},
              {'name': req[2]},
              {'name': req[3]},
              {'name': req[4]},
              {'name': req[5]},
              {'name': req[6]},
              {'name': req[7]},
              {'name': req[8]},
              {'name': req[9]},
              {'name': req[10]},
              {'name': req[11]},
              {'name': req[12]},
              {'name': req[13]},
              {'name': req[14]},
              {'name': req[15]},
              {'name': req[16]},
              {'name': req[17]},
              {'name': req[18]},
              {'name': req[19]}])


@app.route("/response", methods=['GET', 'POST'])
def Response():
    select1 = request.form.get('comp_select1')
    select2 = request.form.get('comp_select2')
    select3 = request.form.get('comp_select3')
    select4 = request.form.get('comp_select4')
    select5 = request.form.get('comp_select5')
    select6 = request.form.get('comp_select6')
    select7 = request.form.get('comp_select7')
    select8 = request.form.get('comp_select8')
    select9 = request.form.get('comp_select9')
    select10 = request.form.get('comp_select10')
    select_all = [select1, select2, select3, select4, select5, select6, select7, select8, select9, select10]
    select = []
    for i in select_all:
        if i != None:
            select.append(i)
        else:
            pass
    return render_template('Response.html', data=[{'output': output(select)[0], 'input': select, 'count': output(select)[2]}])


with open('info.csv', 'r') as f:
    source = f.readlines()

data = []
for i in range(len(source)):
    data.append(source[i].replace("\n", ""))
df = pd.Series(data).str.split(pat=";", expand=True)
df.columns = ["Path",
              "amount_of_shows",
              "category1",
              "category2",
              "category3",
              "category4",
              "category5",
              "category6",
              "category7",
              "category8",
              "category9",
              "category10"
              ]
df['amount_of_shows'] = df['amount_of_shows'].astype(int)
df['amount_of_shows'] = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
print(df)

req = list(set(df.iloc[:, 2:].values.flatten()))
print(req)
log_ind = []


def output(r):
    seq = []
    if r == []:
        top_seq_path = df.iloc[random.randint(0, len(df) - 1), 0]
        ind_top = df.index[df['Path'] == top_seq_path].tolist()
        log_ind.append(ind_top[0])
    else:
        for i in range(len(r)):
            for k in range(10):
                c = df.index[df[f'category{k + 1}'] == r[i]].tolist()
                if c == []:
                    pass
                else:
                    seq.append(c)
        seq_u = list(set([item for sublist in seq for item in sublist]))
        df_t = df.iloc[seq_u].sort_values(by=['amount_of_shows'], ascending=False)
        top_seq_path = df_t.iloc[0, 0]
        ind_top = df.index[df['Path'] == top_seq_path].tolist()
        if log_ind == []:
            pass
        else:
            if ind_top[0] == log_ind[-1]:
                rand_ind = random.randint(0, len(df_t) - 1)
                while log_ind[-1] == rand_ind:
                    rand_ind = random.randint(0, len(df_t) - 1)
                else:
                    top_seq_path = df_t.iloc[rand_ind, 0]
                    ind_top = df.index[df['Path'] == top_seq_path].tolist()
        log_ind.append(ind_top[0])
        df.iloc[ind_top, 1] = df.iloc[ind_top, 1] - 1
        if df.iloc[ind_top, 1].values[0] > 0:
            pass
        else:
            top_seq_path = ''
    return top_seq_path, log_ind, df.iloc[ind_top, 1].values[0]


if __name__ == '__main__':
    app.run(debug=True, port=8080)
