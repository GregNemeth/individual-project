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
        assert 'Banana' in element.text

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
        assert 'Spritz' in element.text

class TestGroup(TestBase):
    def test_add_group(self):
        # navigate to add group page
        self.driver.find_element_by_xpath('/html/body/div[1]/a[3]').click()
        # find and populate text box
        self.driver.find_element_by_xpath('//*[@id="group_name"]').send_keys('genever')       
        # find and add ingredient
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        # check history
        element = self.driver.find_element_by_xpath('/html/body/div[15]')
        assert 'Genever' in element.text

class TestAddrec(TestBase):
    def test_addrec(self):
        # navigate to add recipe page
        self.driver.find_element_by_xpath('/html/body/div[1]/a[2]').click()
        # find and populate text box
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('campari spritz')
        # find and populate text box
        self.driver.find_element_by_xpath('//*[@id="description"]').send_keys('whatnot')
        # find and populate text box
        self.driver.find_element_by_xpath('//*[@id="method"]').send_keys('what')
        # find and click ingredient button
        self.driver.find_element_by_xpath('//*[@id="ings1"]').click()
        # find and click ingredient option button
        self.driver.find_element_by_xpath('//*[@id="ings1"]/option[3]').click()
        # find and click submit button
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        # check history
        element = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]')
        assert 'Campari Spritz' in element.text

class TestDelete(TestBase):
    def test_delete(self):
        # navigate to delete recipe 
        self.driver.find_element_by_xpath('/html/body/div[2]/div/a[1]').click()
        # check recipe not showing on page
        element = self.driver.find_element_by_xpath('/html/body')
        assert 'Spritz' not in element.text

class TestDetails(TestBase):
    def test_detail(self):
        # navigate to details
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/a[3]').click()
        # check content
        element = self.driver.find_element_by_xpath('/html/body/div[2]/h2')
        assert 'Negroni' in element.text

class TestSearchname(TestBase):
    def test_searchname(self):
        # navigate to details
        self.driver.find_element_by_xpath('/html/body/div[1]/a[5]').click()
        # input
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys('negroni')
        self.driver.find_element_by_xpath('//*[@id="search"]').click()
        element = self.driver.find_element_by_xpath('/html/body/div[3]')
        assert 'Negroni' in element.text