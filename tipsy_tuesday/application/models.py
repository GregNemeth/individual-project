from application import db


class CocktailRecipes(db.Model):
    rec_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False)
    method = db.Column(db.String(500), nullable=False)
    junction = db.relationship('R_I_Junction', backref='cocktailRecipes')

class IngredientGroup(db.Model):
    ing_group_id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(40), nullable=False, unique=True)
    ingridients = db.relationship('Ingredients', backref='ingredientGroup')
    junction = db.relationship('R_I_Junction', backref='ing_group')

class Ingredient(db.Model):
    ing_id = db.Column(db.Integer, primary_key=True)
    ing_name = db.Column(db.String(40), nullable=False, unique=True)
    ing_group_id = db.Column(db.Integer, db.ForignKey('ingredientGroup.ing_group_id'), nullable=False)

class Quantity(db.Model):
    quantity_id = db.Column(db.Integer, primary_key=True)
    quantity_ml = db.Column(db.Float, nullable=False, unique=True)
    junction = db.relationship('R_I_Junction', backref='quantity')

class R_I_Junction(db.Model):
    rij_id = db.Column(db.Integer, primary_key=True)
    rec_id = db.Column(db.Integer, db.ForeignKey('cocktailRecipes.rec_id'), nullable=False)
    ing_group_id = db.Column(db.Integer, db.ForignKey('ing_group.ing_group_id'), nullable=False)
    quantity_id = db.Column(db.Integer, db.ForeignKey('quantity.quantity_id'), nullable=False)

class Moderators(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.string(50), nullable=False, unique=True)
    password = db.Column(db.string(100), nullable=False)

