from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class RMSearch(FlaskForm):
    search = StringField('Search', validators=[DataRequired])
