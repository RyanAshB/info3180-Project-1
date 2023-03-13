from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SelectField
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms.validators import DataRequired


class PropertyForm(FlaskForm):
    propTitle = StringField('Title', validators=[DataRequired()])    
    description = TextField('Description', validators=[DataRequired()])
    roomNum = StringField('Number of Rooms', validators=[DataRequired()])
    bathroomNum = StringField('Number of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    propType = SelectField('Category', choices = [('Apartment', 'Apartment'), ('House', 'House')], validators=[DataRequired()])
    file = FileField('Image', validators=[
    	DataRequired(),
    	FileAllowed(['jpg','png','Images Only!'])
    ]) 
    
