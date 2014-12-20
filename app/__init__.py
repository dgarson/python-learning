from flask import Flask

app = Flask('key_binding_app')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/key_bindings.db'

