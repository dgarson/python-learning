__author__ = 'robert'

from flask import flash, redirect, render_template, request, url_for
from .main import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Let Flask-Login know that this user
        # has been authenticated and should be
        # associated with the current session.
        login_user(form.user)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("tracking.index"))
    #return render_template('users/login.html', form=form)
    return "You're logging in..."


@app.route('/signup/', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
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
