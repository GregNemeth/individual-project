from sqlalchemy import join, select
from flask import redirect, request, url_for
from flask.templating import render_template
from application import app, db
from application.models import Cocktailrecipes, Ingredient, Ingredientgroup, Junction, Quantity
from application.forms import AddGroup, AddIngredient, AddRecipe, SearchName, UpdateRecipe


@app.route('/')
def home():
    # add variables to be called on in home.html
    groups = Ingredientgroup.query.all()
    ingredients = Ingredient.query.all()
    recipes = Cocktailrecipes.query.all()
    
    return render_template('home.html', groups=groups, ingredients=ingredients, recipes=recipes)


@app.route('/add_ingredient', methods=["GET", "POST"])
def add_ingredient():
    form = AddIngredient()
    
    if request.method == 'POST':
        new_ingredient = Ingredient(ing_name=form.ingredient.data.title())
        new_ingredient.ing_group_id = form.ing_group.data
        db.session.add(new_ingredient)
        db.session.commit()

        return redirect(url_for('home'))
    
    else:
        ing_groups = Ingredientgroup.query.all()
        form.ing_group.choices = []     # populate selectfields
        for ing_group in ing_groups:
            form.ing_group.choices.append((ing_group.ing_group_id, ing_group.group_name))
        return render_template('add_ingredient.html', form=form)

@app.route('/add_group', methods=["GET", "POST"])
def add_group():
    form = AddGroup()

    if request.method == 'POST':
        new_group = Ingredientgroup(group_name=form.group_name.data.title())
        db.session.add(new_group)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        return render_template('add_group.html', form=form)


@app.route('/add_recipe', methods=["GET", "POST"])
def add_recipe():
    form = AddRecipe()
    aringredients = Ingredient.query.all() # variables for filling in selectfields
    arquants = Quantity.query.all()
    

    if request.method == 'POST':
        new_recipe = Cocktailrecipes(name=form.name.data.title())  # insert row in Cocktailrecipes table
        new_recipe.description = form.description.data
        new_recipe.method = form.method.data

        db.session.add(new_recipe)
        db.session.commit()

        new_junction1 = Junction(rec_id=new_recipe.rec_id)  # create junctions so we can query information from multiple tables, adding ingredients to recipes
        new_junction1.ing_id = form.ings1.data
        new_junction1.quantity_id = form.quants1.data
        new_junction2 = Junction(rec_id=new_recipe.rec_id)
        new_junction2.ing_id = form.ings2.data
        new_junction2.quantity_id = form.quants2.data
        new_junction3 = Junction(rec_id=new_recipe.rec_id)
        new_junction3.ing_id = form.ings3.data
        new_junction3.quantity_id = form.quants3.data
        new_junction4 = Junction(rec_id=new_recipe.rec_id)
        new_junction4.ing_id = form.ings4.data
        new_junction4.quantity_id = form.quants4.data
        new_junction5 = Junction(rec_id=new_recipe.rec_id)
        new_junction5.ing_id = form.ings5.data
        new_junction5.quantity_id = form.quants5.data
        
        junctions = [           # add junctions to db
            new_junction1,
            new_junction2,
            new_junction3,
            new_junction4,
            new_junction5
            ]
        for j in junctions:
            db.session.add(j)
        
        db.session.commit()

        cleanup = Junction.query.filter_by(ing_id=1).all()      # removes unpopulated rows in junction table
        for items in cleanup:

            db.session.delete(items)
        db.session.commit()
        
        return(redirect(url_for('home')))

    else:
           
        form.ings1.choices = [(ingredient.ing_id, ingredient.ing_name) for ingredient in aringredients]  # populate selectfields
        form.quants1.choices = [(quantity.quantity_id, quantity.quantity_ml) for quantity in arquants]
        form.ings2.choices = [(ingredient.ing_id, ingredient.ing_name) for ingredient in aringredients]
        form.quants2.choices = [(quantity.quantity_id, quantity.quantity_ml) for quantity in arquants]
        form.ings3.choices = [(ingredient.ing_id, ingredient.ing_name) for ingredient in aringredients]
        form.quants3.choices = [(quantity.quantity_id, quantity.quantity_ml) for quantity in arquants]
        form.ings4.choices = [(ingredient.ing_id, ingredient.ing_name) for ingredient in aringredients]
        form.quants4.choices = [(quantity.quantity_id, quantity.quantity_ml) for quantity in arquants]
        form.ings5.choices = [(ingredient.ing_id, ingredient.ing_name) for ingredient in aringredients]
        form.quants5.choices = [(quantity.quantity_id, quantity.quantity_ml) for quantity in arquants]
        

        return render_template('add_recipe.html', form=form)
        

@app.route('/delete/<rec_id>')
def delete_recipe(rec_id):
    selected_recipe = Cocktailrecipes.query.get(rec_id)     # identify recipe
    selected_junction = Junction.query.filter_by(rec_id=selected_recipe.rec_id).all()   # and all juntions belonging to selected recipe

    db.session.delete(selected_recipe)
                                            # remove recipe and junctions
    for items in selected_junction:
        db.session.delete(items)
    db.session.commit()
    
    return redirect(url_for('home'))

@app.route('/update_recipe/<rec_id>', methods=['GET','POST'])       
def update_recipe(rec_id):
    current_recipe = Cocktailrecipes.query.get(rec_id)      # get current recipe id
    form = UpdateRecipe()
    aringredients = Ingredient.query.all()      # required to populate selectfields
    arquants = Quantity.query.all()

    if request.method == 'POST':
        current_recipe.name = form.name.data.title()        # Populate the name, desc. and method of recipe so we have a better understandning on what we are editing
        current_recipe.description = form.description.data
        current_recipe.method = form.method.data
        
        drop_old_junction = Junction.query.filter_by(rec_id=current_recipe.rec_id).all()    # remove old junctions so we can work with the updated ingredients
        
        for oj in drop_old_junction:
            db.session.delete(oj)
        db.session.commit()
        
       
        new_junction1 = Junction(rec_id=current_recipe.rec_id)
        new_junction1.ing_id = form.ings1.data
        new_junction1.quantity_id = form.quants1.data
        new_junction2 = Junction(rec_id=current_recipe.rec_id)
        new_junction2.ing_id = form.ings2.data
        new_junction2.quantity_id = form.quants2.data
        new_junction3 = Junction(rec_id=current_recipe.rec_id)
        new_junction3.ing_id = form.ings3.data
        new_junction3.quantity_id = form.quants3.data
        new_junction4 = Junction(rec_id=current_recipe.rec_id)
        new_junction4.ing_id = form.ings4.data
        new_junction4.quantity_id = form.quants4.data
        new_junction5 = Junction(rec_id=current_recipe.rec_id)
        new_junction5.ing_id = form.ings5.data
        new_junction5.quantity_id = form.quants5.data
        
        junctions = [
            new_junction1,
            new_junction2,
            new_junction3,
            new_junction4,
            new_junction5
            ]
        for j in junctions:
            db.session.add(j)
        
        db.session.commit()
        cleanup = Junction.query.filter_by(ing_id=1).all()
        for items in cleanup:
            db.session.delete(items)
        db.session.commit()
        
        return(redirect(url_for('home')))

    else:
        form.name.data = current_recipe.name
        form.description.data = current_recipe.description
        form.method.data = current_recipe.method
        form.ings1.choices = [(ingredient.ing_id, ingredient.ing_name) for ingredient in aringredients]
        form.quants1.choices = [(quantity.quantity_id, quantity.quantity_ml) for quantity in arquants]      # some comment here
        form.ings2.choices = [(ingredient.ing_id, ingredient.ing_name) for ingredient in aringredients]
        form.quants2.choices = [(quantity.quantity_id, quantity.quantity_ml) for quantity in arquants]
        form.ings3.choices = [(ingredient.ing_id, ingredient.ing_name) for ingredient in aringredients]
        form.quants3.choices = [(quantity.quantity_id, quantity.quantity_ml) for quantity in arquants]
        form.ings4.choices = [(ingredient.ing_id, ingredient.ing_name) for ingredient in aringredients]
        form.quants4.choices = [(quantity.quantity_id, quantity.quantity_ml) for quantity in arquants]
        form.ings5.choices = [(ingredient.ing_id, ingredient.ing_name) for ingredient in aringredients]
        form.quants5.choices = [(quantity.quantity_id, quantity.quantity_ml) for quantity in arquants]
        

        return render_template('update_recipe.html', form=form)

@app.route('/show_details/<rec_id>')
def show_details(rec_id):
    dictionary = {}         # catch output from loop
    selected_recipe = Cocktailrecipes.query.get(rec_id)     # get recipe id, ingredients and quantities with query
    ings_quants = db.session.query(Ingredient,Quantity)\
        .select_from(join(Ingredient, Junction))\
        .join(Cocktailrecipes, Cocktailrecipes.rec_id == Junction.rec_id)\      
        .join(Quantity, Quantity.quantity_id == Junction.quantity_id)\
        .filter(Junction.rec_id==selected_recipe.rec_id).all()

    for i, q in ings_quants:    # loop through query output and convert it to dictionary so we can use the variables in the html file
        dictionary[i] = q

    return render_template('details.html', selected_recipe=selected_recipe, dictionary=dictionary)

@app.route('/search_by_name', methods=['GET','POST'])
def search():
    form = SearchName()
    recipes = Cocktailrecipes.query.all()       # so we can use details link
    target = form.name.data.title()     # input from form
    
    
    if request.method == 'POST':
        resultname = db.session.query(Cocktailrecipes).filter_by(name=target).all()
        return render_template('search_by_name.html', resultname=resultname, form=form,  recipes=recipes)
        

    else:
        resultname = db.session.query(Cocktailrecipes).filter_by(name=target).all()
        return render_template('search_by_name.html', form=form, resultname=resultname)

# @app.route('/search_by_group', methods=['GET','POST'])
# def search_by_group():
    
#     return 'group'

# @app.route('/search_by_ing', methods=['GET','POST'])
# def search_by_ing():
    
#     return 'ingredient'