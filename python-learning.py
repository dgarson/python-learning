from flask import Flask

databaseUri = "sqlite:////tmp/key_bindings.db"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = databaseUri
print('configured Flask app with databaseUri', app.config['SQLALCHEMY_DATABASE_URI'])

from app.database import db_session, init_db

init_db()
print('initialized database.')

from app.utils import UserFile

# process default user file to populate database (has plaintext passwords: only for testing!)
defUsers = UserFile("defaultUsers.xml")
defUsers.process()

# make sure to teardown any database-connections at the end of each request
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # app.debug = True
    from app.security import *
    app.run()