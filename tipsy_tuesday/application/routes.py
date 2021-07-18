from flask import Blueprint
from flask import redirect, request, url_for
from application import app, db
from applicaton.models import CocktailRecipes, IngredientGroup, Ingredient, Quantity, R_I_Junction

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return 'Home'


