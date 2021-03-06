from flask import Flask

secretKey = b'\xff\x02\xf5;\xe9\x00+;\xc9\xde\x08Re\xfe\x90\xb8{\x1a!\x0e\xe6EH\xee'
databaseUri = "sqlite:////tmp/key_bindings.db"
app = Flask(__name__)
app.config['SECRET_KEY'] = secretKey
app.config['DEBUG'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True
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
