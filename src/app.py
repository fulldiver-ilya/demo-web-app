from flask import Flask

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def hello_world():
    return app.send_static_file('index.html')
