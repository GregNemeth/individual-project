from enum import unique
from application import db


class CocktailRecipes(db.Model):
    rec_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False)
    method = db.Column(db.String(500), nullable=False)

class IngredientGroup(db.Model):
    ing_group_id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(40), nullable=False, unique=True)
    ingridients = db.relationship('Ingredients', backref='ingredientGroup')

class Ingredient(db.Model):
    ing_id = db.Column(db.Integer, primary_key=True)
    ing_name = db.Column(db.String(40), nullable=False, unique=True)
    ing_group_id = db.Column(db.Integer, db.ForignKey('ingredientGroup.ing_group_id'), nullable=False)

class Quantity(db.Model):
    quantity_id = db.Column(db.Integer, primary_key=True)
    quantity_ml = db.Column(db.Float, nullable=False, unique=True)

class R_I_Junctrion(db.Model):
    rij_id = db.Column(db.Integer, primary_key=True)
