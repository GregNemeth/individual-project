from application.models import Ingredientgroup, Cocktailrecipes, Ingredient, Junction, Quantity
from application import db

db.drop_all()
db.create_all()

db.session.add(Ingredientgroup(group_name=None))
db.session.add(Ingredient(ing_name=None))


quants = ('1.5','4.5','10','15','25','30','35','40','50','60')

for quantity in quants:
    db.session.add(Quantity(quantity_ml=quantity))
    
db.session.commit()

groups = ('Gin','Rum','Tequila','Whisky','Vodka','Vermouth','Liquor','Amaro','Bitter','Soft Drink','Dry Ingredient',)
for group in groups:
    db.session.add(Ingredientgroup(group_name=group))

db.session.commit()