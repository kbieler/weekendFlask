#when you want to do testing throught the flask shell with this context processor
#change the FLASK_APP variable in .env to run.py

from app import app
from app.models import db, Whatsit, User

@app.shell_context_processor
def shell_context():
    return {'db': db, 'Whatsit': Whatsit, 'User': User}


