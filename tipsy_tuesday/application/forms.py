from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class AddIngredient(FlaskForm):
    ingredient = StringField('Ingredient here')
    ing_group = SelectField('Choose ingredient group', choices=[])
    submit = SubmitField('Add ingredient')

class AddGroup(FlaskForm):
    group_name = StringField('Ingredient Group')
    submit = SubmitField('Add Group')
