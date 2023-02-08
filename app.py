from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello world</h1>'

@app.route('/index')
def index():
    return '<h1>Index: 203</h1>'
@app.route('/home')
def home():
    return '<h1>Flask homework</h1>'

if __name__ == '__main__':
    app.run()