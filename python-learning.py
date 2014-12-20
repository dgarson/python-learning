from flask import Flask

databaseUri = "sqlite:////tmp/key_bindings.db"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = databaseUri
print('configured Flask app with databaseUri', app.config['SQLALCHEMY_DATABASE_URI'])

from app.database import db_session, init_db

init_db()
print('initialized database.')

from app.utils import UserFile

defUsers = UserFile("defaultUsers.xml")
defUsers.process()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.shutdown()

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    # app.debug = True
    app.run()