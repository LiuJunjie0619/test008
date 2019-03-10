# -*- encoding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'V1.1!'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008, debug=True)
