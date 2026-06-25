# Demo
from flask import Flask, render_template
app = Flask(__name__)
return X



@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'
