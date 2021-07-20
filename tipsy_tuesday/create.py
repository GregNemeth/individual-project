from application.models import Ingredientgroup, Cocktailrecipes, Ingredient, Junction, Quantity
from application import db

db.drop_all()
db.create_all()

