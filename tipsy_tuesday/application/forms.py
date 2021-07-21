from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField,  Form


class AddIngredient(FlaskForm):
    ingredient = StringField('Ingredient here')
    ing_group = SelectField('Choose ingredient group', choices=[])
    submit = SubmitField('Add ingredient')

class AddGroup(FlaskForm):
    group_name = StringField('Ingredient Group')
    submit = SubmitField('Add Group')


class AddRecipe(FlaskForm):
    name = StringField('Recipe name')
    description = StringField('Recipe description')
    method = StringField('how its done')
    ings1 = SelectField("Ingreds", choices=[])
    quants1 = SelectField('choose quantity', choices=[])
    ings2 = SelectField("Ingreds", choices=[])
    quants2 = SelectField('choose quantity', choices=[])
    ings3 = SelectField("Ingreds", choices=[])
    quants3 = SelectField('choose quantity', choices=[])
    ings4 = SelectField("Ingreds", choices=[])
    quants4 = SelectField('choose quantity', choices=[])
    ings5 = SelectField("Ingreds", choices=[])
    quants5 = SelectField('choose quantity', choices=[])
    
    submit = SubmitField('add/update recipe')

class UpdateRecipe(FlaskForm):
    name = StringField('Recipe name', default='')
    description = StringField('Recipe description', default='')
    method = StringField('how its done', default='')
    ings1 = SelectField("Ingreds", choices=[])
    quants1 = SelectField('choose quantity', choices=[])
    ings2 = SelectField("Ingreds", choices=[])
    quants2 = SelectField('choose quantity', choices=[])
    ings3 = SelectField("Ingreds", choices=[])
    quants3 = SelectField('choose quantity', choices=[])
    ings4 = SelectField("Ingreds", choices=[])
    quants4 = SelectField('choose quantity', choices=[])
    ings5 = SelectField("Ingreds", choices=[])
    quants5 = SelectField('choose quantity', choices=[])
    
    submit = SubmitField('add/update recipe')

