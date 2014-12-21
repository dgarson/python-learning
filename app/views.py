from flask_login import LoginManager, login_user, login_required, logout_user
from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import app
from app.models import Account
from app.database import db, db_session
from app.forms import LoginForm, RegistrationForm

__author__ = 'dgarson'

login_manager = LoginManager()
# login_manager.login_view = 'users.login'
login_manager.init_app(app)

users = Blueprint('users', __name__)

@login_manager.user_loader
def load_user(userid):
    return Account.query.get(userid)


@app.route('/')
def index():
    return render_template('index.html')

