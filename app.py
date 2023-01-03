from flask import Flask
from flask import render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route("/")
def example():
    return render_template('example.html', styles=['css/style.css'], scripts=['js/script.js'])
