from application.models import Ingredientgroup, Cocktailrecipes, Ingredient, R_I_Junction, Quantity
from application import db

db.drop_all()
db.create_all()

db.session.add(Ingredientgroup(group_name='Rum'))
db.session.add(Ingredientgroup(group_name='Whiskey'))
db.session.add(Ingredientgroup(group_name='Gin'))
db.session.add(Ingredientgroup(group_name='Tequila'))

db.session.commit()