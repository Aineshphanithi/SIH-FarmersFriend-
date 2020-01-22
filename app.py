from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/register.html')
def register():
    return render_template('register.html')


@app.route('/weatherupdates.html')
def weaterupdates():
    return render_template('weatherupdates.html')


@app.route('/smartguide.html')
def smartguide():
    return render_template('smartguide.html')


if __name__ == "__main__":
    app.run(debug=True)