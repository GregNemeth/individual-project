from application.models import Ingredientgroup, Cocktailrecipes, Ingredient, Junction, Quantity
from application import db

db.drop_all()
db.create_all()

db.session.add(Quantity(quantity_ml='1.5'))
db.session.add(Quantity(quantity_ml='25'))
db.session.add(Quantity(quantity_ml='30'))
db.session.add(Quantity(quantity_ml='35'))
db.session.add(Quantity(quantity_ml='40'))
db.session.add(Quantity(quantity_ml='50'))
db.session.add(Quantity(quantity_ml='60'))
db.session.commit()

db.session.add(Ingredientgroup(group_name='Gin'))
db.session.add(Ingredientgroup(group_name='Rum'))
db.session.add(Ingredientgroup(group_name='Tequila'))
db.session.add(Ingredientgroup(group_name='Vodka'))
db.session.add(Ingredientgroup(group_name='Whisky'))
db.session.add(Ingredientgroup(group_name='Vermouth'))
db.session.add(Ingredientgroup(group_name='Liquor'))
db.session.add(Ingredientgroup(group_name='Amaro'))
db.session.add(Ingredientgroup(group_name='Bitter'))
db.session.add(Ingredientgroup(group_name='Soft Drink'))
db.session.add(Ingredientgroup(group_name='Dry Ingredient'))
db.session.commit()