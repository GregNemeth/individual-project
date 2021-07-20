from application.routes import add_group
from os import name
from flask.helpers import url_for

from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase

from application import app, db
from application.models import Junction, Cocktailrecipes, Ingredientgroup, Ingredient, Quantity

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
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

    def tearDown(self):
        db.drop_all

class TestViews(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
    
    def test_addingredient(self):
        response = self.client.get(url_for('add_ingredient'))
        self.assert200(response)

    def test_addgroup(self):
        response = self.client.get(url_for(add_group))
        self.assert200(response)

