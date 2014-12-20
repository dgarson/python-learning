__author__ = 'robert'

from flask.ext.login import LoginManager

from mrd.users.models import User

login_manager = LoginManager()

login_manager.login_view = "users.login"
# We have not created the users.login view yet
# but that is the name that we will use for our
# login view, so we will set it now.


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = b'\xff\x02\xf5;\xe9\x00+;\xc9\xde\x08Re\xfe\x90\xb8{\x1a!\x0e\xe6EH\xee'

