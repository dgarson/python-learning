__author__ = 'robert'

from flask import flash, redirect, render_template, request, url_for
from .main import app
from .models import Account
from .database import db
from .forms import LoginForm, RegistrationForm
from flask_login import login_user, login_required, logout_user
from app import app

@app.route('/')
def index():
    return render_template('index.html')

