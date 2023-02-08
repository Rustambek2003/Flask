from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello world</h1>'

@app.route('/index')
def index():
    return '<h1>Index route</h1>'
@app.route('/home')
def home():
    return '<h1>Home route</h1>'

if __name__ == '__main__':
    app.run()