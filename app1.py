from flask import Flask, request, render_template

import pickle

app = Flask(__name__)

rainfall_model = pickle.load(open('Rainfall/rangareddi_jan_rainfall.pkl', 'rb'))


@app.route('/')
def home():
    print(rainfall_model.predict([[2025]])[0])

    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/register.html')
def register():
    return render_template('register.html')


@app.route('/weatherupdates.html')
def weatherupdates():
    return render_template('weatherupdates.html')


@app.route('/smartguide.html')
def smartguide():
    return render_template('smartguide.html')


if __name__ == "__main__":
    app.run(debug=True)