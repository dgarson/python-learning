from app import app
from flask import Flask, render_template, redirect, url_for, request
from flask_login import login_required

app = Flask(__name__)


app.run()

