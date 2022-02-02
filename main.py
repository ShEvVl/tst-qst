from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)


@app.route('/')
@app.route('/request', methods=['GET', 'POST'])
def form():
    # handle the POST request
    if request.method == 'POST':
        category1 = request.form.get('category1')
        category2 = request.form.get('category2')
        category3 = request.form.get('category3')
        category4 = request.form.get('category4')
        category5 = request.form.get('category5')
        category6 = request.form.get('category6')
        category7 = request.form.get('category7')
        category8 = request.form.get('category8')
        category9 = request.form.get('category9')
        category10 = request.form.get('category10')
        return '''<h1>You choose: <br> {}.</h1><br>
        <image src = "http://localhost:8080/static/image1.jpg">'''.format(', '.join([
            category1,
            category2,
            category3,
            category4,
            category5,
            category6,
            category7,
            category8,
            category9,
            category10
        ]))

    return '''<h1>Choose several categories from the list: <br> {}</h1>
            <form method="POST">
            Category1 <input type="text" name="category1"><br>            
            Category2 <input type="text" name="category2"><br> 
            Category3 <input type="text" name="category3"><br> 
            Category4 <input type="text" name="category4"><br> 
            Category5 <input type="text" name="category5"><br> 
            Category6 <input type="text" name="category6"><br> 
            Category7 <input type="text" name="category7"><br> 
            Category8 <input type="text" name="category8"><br> 
            Category9 <input type="text" name="category9"><br> 
            Category10 <input type="text" name="category10"><br> 
            <input type="submit"><br> 
            </form>'''.format(', '.join(categories))


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
print(df)
categories = ('apple',
              'banana',
              'city',
              'drill',
              'ear',
              'forest',
              'gim',
              'hill',
              'ink',
              'juice',
              'koala',
              'lion',
              'mouse',
              'notebook',
              'octopus',
              'panda',
              'queen',
              'rabbit',
              'sun',
              'tea')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
