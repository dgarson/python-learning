from flask import Flask
from app.database import db_session, init_db

app = Flask('key_binding_app')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/key_bindings.db'
print('configured Flask app')

init_db()
print('initialized database.')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.shutdown()

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()