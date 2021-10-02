from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Book:')
    author = StringField("Name of Author:")
    submit = SubmitField('Add Book')

class BuyForm(FlaskForm):
    
    id = IntegerField('Id Number of book to buy:')
    submit = SubmitField('Purchase Book')