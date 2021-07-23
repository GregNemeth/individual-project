from application.models import  Cocktailrecipes,Ingredientgroup, Ingredient, Junction, Quantity
from application import db

db.drop_all()
db.create_all()

db.session.add(Ingredientgroup(group_name=None))
db.session.add(Ingredient(ing_name=None))


quants = ('1.5','4.5','10','15','25','30','35','40','50','60')

for quantity in quants:
    db.session.add(Quantity(quantity_ml=quantity))
    
db.session.commit()

groups = (
    'Gin',
    'Rum',
    'Tequila',
    'Whisky',
    'Vodka',
    'Vermouth',
    'Liquor',
    'Amaro',
    'Bitter',
    'Soft Drink',
    'Dry Ingredient'
    )
for group in groups:
    db.session.add(Ingredientgroup(group_name=group))

jensens = Ingredient(ing_name="Jensen's Old Tom")
jensens.ing_group_id = 2
db.session.add(jensens)
vermouth = Ingredient(ing_name="Punt e Mes")
vermouth.ing_group_id = 7
db.session.add(vermouth)
campari = Ingredient(ing_name="Campari")
campari.ing_group_id = 9
db.session.add(campari)
db.session.add(
    Cocktailrecipes(
    name='Negroni',
    description='Bittersweet aperitivo',
    method='stir until chilled and strain onto fresh ice')
    )

junctions = [
    Junction(rec_id=1,ing_id=2,quantity_id=6),
    Junction(rec_id=1,ing_id=3,quantity_id=5),
    Junction(rec_id=1,ing_id=4,quantity_id=5)
    ]

for j in junctions:
    db.session.add(j)

db.session.commit()

