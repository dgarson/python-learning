from app import app
from flask import Flask, session, redirect, url_for, escape, request
from utils.mrd.auth import login_manager

app = Flask(__name__)
login_manager.init_app(app)

@app.route('/')
def index():
    return 'Welcome to the app!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login and validate the user...
        login_user(user)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("index"))
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

