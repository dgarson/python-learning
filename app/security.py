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

@app.route("/login/", methods=["GET", "POST"])
def login():
    print("login")
    form = LoginForm()
    print("form created")
    if form.validate_on_submit():
        login("validated - logging in user")
        # Let Flask-Login know that this user
        # has been authenticated and should be
        # associated with the current session.
        login_user(form.user)
        flash("Logged in successfully.")
        print("Login validation succeeded")
        return redirect(request.args.get("next") or url_for("tracking.index"))
    return render_template('login.html', form=form, error=None)

@users.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Account()
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('tracking.index'))
    return render_template('register.html', form=form)


@users.route('/logout/')
@login_required
def logout():
    # Tell Flask-Login to destroy the
    # session->User connection for this session.
    logout_user()
    return redirect(url_for('tracking.index'))