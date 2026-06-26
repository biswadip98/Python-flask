# Demo application for linter
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'

# This app will run on self-hosted runner, instead of Ubuntu-Latest.