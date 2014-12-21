from app import app

# app.debug = True
from app.security import *
from app.views import *

app.run()