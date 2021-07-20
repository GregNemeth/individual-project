from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FormField, FieldList, Form


class AddIngredient(FlaskForm):
    ingredient = StringField('Ingredient here')
    ing_group = SelectField('Choose ingredient group', choices=[])
    submit = SubmitField('Add ingredient')

class AddGroup(FlaskForm):
    group_name = StringField('Ingredient Group')
    submit = SubmitField('Add Group')

class Ingreds(Form):
    ingredient = SelectField('choose ingredient', choices=[])
    quantity = SelectField('choose quantity', choices=[])

class AddRecipe(FlaskForm):
    name = StringField('Recipe name')
    description = StringField('Recipe description')
    method = StringField('how its done')
    ings = FieldList(FormField(Ingreds), min_entries=3)
    
    submit = SubmitField('add recipe')

