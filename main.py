from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)


@app.route('/')
@app.route('/request')
def request():
    return render_template('request.html')


@app.route('/response')
def response():
    return render_template('response.html')


with open('info.csv', 'r') as f:
    source = f.readlines()

data = []
for i in range(len(source)):
    data.append(source[i].replace("\n", ""))
df = pd.Series(data).str.split(pat=";", expand=True)
df.columns = ["Path",
              "needed_amount_of_shows",
              "category_1",
              "category_2",
              "category_3",
              "category_4",
              "category_5",
              "category_6",
              "category_7",
              "category_8",
              "category_9",
              "category_10"
              ]
print(df)

if __name__ == '__main__':
    app.run(debug=True)
