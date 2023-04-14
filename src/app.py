from flask import Flask

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p><a href='static/index.html'>open</a>"