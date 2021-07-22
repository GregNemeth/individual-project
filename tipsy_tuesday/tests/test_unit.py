from application.routes import add_group, add_recipe, add_ingredient, home, update_recipe, delete_recipe
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

        jensens = Ingredient(ing_name="Jensen's Old Tom")
        jensens.ing_group_id = 2
        db.session.add(jensens)
        vermouth = Ingredient(ing_name="Punt e Mes")
        vermouth.ing_group_id = 7
        db.session.add(vermouth)
        campari = Ingredient(ing_name="Campari")
        campari.ing_group_id = 9
        db.session.add(campari)

        db.session.add(Cocktailrecipes(name='Negroni', description='Bittersweet aperitivo', method='stir until chilled and strain onto fresh ice'))
        junction1 = Junction(rec_id=1,ing_id=2,quantity_id=6)
        junction2= Junction(rec_id=1,ing_id=3,quantity_id=5)
        junction3= Junction(rec_id=1,ing_id=4,quantity_id=5)
        db.session.add(junction1)
        db.session.add(junction2)
        db.session.add(junction3)
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
        response = self.client.get(url_for('add_group'))
        self.assert200(response)

    def test_addrecipe(self):
        response = self.client.get(url_for('add_recipe'))
        self.assert200(response)

    def test_updaterecipe(self):
        response = self.client.get(url_for('update_recipe', rec_id=1))
        self.assert200(response)

    def test_deleterecipe(self):
        response = self.client.get(url_for('delete_recipe', rec_id=1))
        self.assertEqual(response.status_code, 302)

class TestRead(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))

        assert "Negroni" in response.data.decode()
        assert "Recipes added" in response.data.decode()
        

class TestCreate(TestBase):
    def test_addingred(self):
        response = self.client.post(
            url_for('add_ingredient'),
            data={'ingredient':'dingle'},
            follow_redirects=True
            )

        assert 'dingle' in response.data.decode()

class TestCreateGroup(TestBase):
    def test_addgroup(self):
        response = self.client.post(
            url_for('add_group'),
            data={'group_name':'decoration'},
            follow_redirects=True
            )

        assert 'decoration' in response.data.decode()

class TestCreateRecipe(TestBase):
    def test_addrec(self):
        response = self.client.post(
            url_for('add_recipe'),
            data={'description':'sweet',
                  'ings1':2,
                  'ings2':3,
                  'ings3':1,
                  'ings4':1,
                  'ings5':1,
                  'method':'stir',
                  'name':'martinez',
                  'quants1':10,
                  'quants2':5,
                  'quants3':1,
                  'quants4':1,
                  'quants5':1,
                  'submit':'add/update recipe'

                  },
            follow_redirects=True
            )

        assert 'martinez' in response.data.decode()

class TestDelete(TestBase):
    def test_delete(self):
        response = self.client.get(
            url_for('delete_recipe', rec_id=1),
            follow_redirects=True
        )

        assert 'Negroni' not in response.data.decode()

class TestupdateRecipe(TestBase):
    def test_updaterec(self):
        response = self.client.post(
            url_for('update_recipe', rec_id=1),
            data={'description':'sweet',
                  'ings1':2,
                  'ings2':3,
                  'ings3':1,
                  'ings4':1,
                  'ings5':1,
                  'method':'stir',
                  'name':'martini',
                  'quants1':10,
                  'quants2':5,
                  'quants3':1,
                  'quants4':1,
                  'quants5':1,
                  'submit':'add/update recipe'

                  },
            follow_redirects=True
            )

        assert 'martini' in response.data.decode()



