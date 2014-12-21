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
    return(733)
    return render_template('index.html')

@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login and validate the user...
        login_user(form.user)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("index"))
    return render_template("login.html", form=form)

@app.route('/register/', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Account()
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('tracking.index'))
    return render_template('users/register.html', form=form)


@app.route('/logout/')
@login_required
def logout():
    # Tell Flask-Login to destroy the
    # session->User connection for this session.
    logout_user()
    return redirect(url_for('tracking.index'))

@app.route('/')
def index():
    return render_template('index.html')

