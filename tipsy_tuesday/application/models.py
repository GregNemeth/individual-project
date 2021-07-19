from application import db

class Junction(db.Model):
    rij_id = db.Column(db.Integer, primary_key=True)
    rec_id = db.Column(db.Integer, db.ForeignKey('cocktail.rec_id'), nullable=False)
    ing_id = db.Column(db.Integer, db.ForeignKey('ingredient.ing_id'), nullable=False)
    quantity_id = db.Column(db.Integer, db.ForeignKey('quantity.quantity_id'), nullable=False)

class Cocktailrecipes(db.Model):
    rec_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False)
    method = db.Column(db.String(500), nullable=False)
    junction = db.relationship('Junction', backref='cocktail')

class Ingredientgroup(db.Model):
    ing_group_id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(40), nullable=False, unique=True)
    ingridients = db.relationship('Ingredient', backref='ingredientGroup')
    

class Ingredient(db.Model):
    ing_id = db.Column(db.Integer, primary_key=True)
    ing_name = db.Column(db.String(40), nullable=False, unique=True)
    ing_group_id = db.Column(db.Integer, db.ForeignKey('ingredientGroup.ing_group_id'), nullable=False)
    junction = db.relationship('Junction', backref='ingredient')

class Quantity(db.Model):
    quantity_id = db.Column(db.Integer, primary_key=True)
    quantity_ml = db.Column(db.Float, nullable=False, unique=True)
    junction = db.relationship('Junction', backref='quantity')



# class Moderators(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     fname = db.Column(db.String(20), nullable=False)
#     lname = db.Column(db.String(30), nullable=False)
#     email = db.Column(db.String(50), nullable=False, unique=True)
#     password = db.Column(db.String(100), nullable=False)

