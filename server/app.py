from logging import DEBUG
from flask import Flask, json, jsonify
from flask_cors import CORS

# config settings
DEBUG = True

# start app
app = Flask(__name__)
app.config.from_object(__name__)

# CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/ping', methods=['GET'])
def ping_pong():
    return "<h2>YOU ARE A DEVILS</h2>"


if __name__ == "__main__":
    app.run()