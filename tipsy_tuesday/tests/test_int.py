from os import name
from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen

from flask import url_for
from application import app, db
from application.models import Junction, Cocktailrecipes, Ingredientgroup, Ingredient, Quantity

class TestBase(LiveServerTestCase):
    TEST_PORT = 5050

    def create_app(self):
        

        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            LIVESERVER_PORT=self.TEST_PORT,
            WTF_CSRF_ENABLED=False,
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            DEBUG=True,
            TESTING=True
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

        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options)

        

        self.driver.get(f'http://localhost:{self.TEST_PORT}')

    def tearDown(self):

        self.driver.quit()

        db.drop_all()

    def test_server_is_up_and_running(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}')
        self.assertEqual(response.code, 200)

class TestCreate(TestBase):
    def test_add_ing(self):
        # navigate to create page
        self.driver.find_element_by_xpath('/html/body/div[1]/a[4]').click()
        # find and populate text box
        self.driver.find_element_by_xpath('//*[@id="ingredient"]').send_keys('banana')
        # find and click selectfield 
        self.driver.find_element_by_xpath('//*[@id="ing_group"]').click()
        # find and click choice 
        self.driver.find_element_by_xpath('//*[@id="ing_group"]/option[12]').click()
        # find and add ingredient
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        # check history
        element = self.driver.find_element_by_xpath('/html/body/div[19]')
        assert 'banana' in element.text

class TestUpdate(TestBase):
    def test_updaterec(self):
        # navigate to update page
        self.driver.find_element_by_xpath('/html/body/div[2]/div/a[2]').click()
        # find and populate text box
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(' spritz')
        # find and click ingredient button
        self.driver.find_element_by_xpath('//*[@id="ings1"]').click()
        # find and click ingredient option button
        self.driver.find_element_by_xpath('//*[@id="ings1"]/option[4]').click()
        # find and click submit button
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        # check history
        element = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]')
        assert 'spritz' in element.text
