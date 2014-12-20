from app import app
from flask import Flask, render_template, session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.run()

