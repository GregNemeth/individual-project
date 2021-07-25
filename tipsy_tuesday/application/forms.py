from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired


class AddIngredient(FlaskForm):
    ingredient = StringField('Ingredient here', validators=[DataRequired()])
    ing_group = SelectField('Choose ingredient group', choices=[])
    submit = SubmitField('Add ingredient')

class AddGroup(FlaskForm):
    group_name = StringField('Ingredient Group')
    submit = SubmitField('Add Group')


class AddRecipe(FlaskForm):
    name = StringField('Recipe name', validators=[DataRequired()])
    description = StringField('Recipe description', validators=[DataRequired()])
    method = StringField('how its done', validators=[DataRequired()])
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

class SearchName(FlaskForm):
    name = StringField('Enter recipe name to search', default='', validators=[DataRequired()])
    search = SubmitField('search now')



