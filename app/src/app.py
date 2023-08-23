from flask import Flask, jsonify
import os
import socket


app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify(message="This is simple flask app")


@app.route('/hostname')
def get_hostname_container():
    return jsonify(hostname=socket.gethostname())


@app.route('/author')
def get_author():
    author = os.environ.get('AUTHOR', 'Unknown')
    return jsonify(author=author)


@app.route('/id')
def get_id():
    uid = os.environ.get('UID')
    if not uid:
        return "UID not found", 503
    return jsonify(id=uid)


# ставим liveness probe:
# приложение is alive:

@app.route('/healthz')
def send_healthz():
    return "OK", 200


# ставим readiness probe:


@app.route('/readiness')
def uid_readiness():
    return "OK", 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
