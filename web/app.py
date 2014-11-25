#-*- coding:utf-8 -*-
from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', **locals())


@app.route('/data/<path:filename>')
def data(filename):
    return send_from_directory('data', filename)


if __name__ == "__main__":
    app.run()
