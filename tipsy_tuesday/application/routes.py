from sqlalchemy import join, select
from flask import redirect, request, url_for
from flask.templating import render_template
from application import app, db
from application.models import Cocktailrecipes, Ingredient, Ingredientgroup, Junction, Quantity
from application.forms import AddGroup, AddIngredient, AddRecipe, UpdateRecipe


@app.route('/')
def home():

    groups = Ingredientgroup.query.all()
    ingredients = Ingredient.query.all()
    recipes = Cocktailrecipes.query.all()
    
    return render_template('home.html', groups=groups, ingredients=ingredients, recipes=recipes)


@app.route('/add_ingredient', methods=["GET", "POST"])
def add_ingredient():
    form = AddIngredient()
    
    if request.method == 'POST':
        new_ingredient = Ingredient(ing_name=form.ingredient.data)
        new_ingredient.ing_group_id = form.ing_group.data
        db.session.add(new_ingredient)
        db.session.commit()

        return redirect(url_for('home'))
    
    else:
        ing_groups = Ingredientgroup.query.all()
        form.ing_group.choices = []
        for ing_group in ing_groups:
            form.ing_group.choices.append((ing_group.ing_group_id, ing_group.group_name))
        return render_template('add_ingredient.html', form=form)

@app.route('/add_group', methods=["GET", "POST"])
def add_group():
    form = AddGroup()

    if request.method == 'POST':
        new_group = Ingredientgroup(group_name=form.group_name.data)
        db.session.add(new_group)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        return render_template('add_group.html', form=form)


@app.route('/add_recipe', methods=["GET", "POST"])
def add_recipe():
    form = AddRecipe()
    aringredients = Ingredient.query.all()
    arquants = Quantity.query.all()
    

    if request.method == 'POST':
        new_recipe = Cocktailrecipes(name=form.name.data)
        new_recipe.description = form.description.data
        new_recipe.method = form.method.data
        db.session.add(new_recipe)
        db.session.commit()
        new_junction1 = Junction(rec_id=new_recipe.rec_id)
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
        
        db.session.add(new_junction1)
        db.session.add(new_junction2)
        db.session.add(new_junction3)
        db.session.add(new_junction4)
        db.session.add(new_junction5)
        db.session.commit()
        cleanup = Junction.query.filter_by(ing_id=1).all()
        for items in cleanup:
            db.session.delete(items)
        db.session.commit()
        
        return(redirect(url_for('home')))

    else:
           
        form.ings1.choices = [(ingredient.ing_id, ingredient.ing_name) for ingredient in aringredients]
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
    selected_recipe = Cocktailrecipes.query.get(rec_id)
    selected_junction = Junction.query.filter_by(rec_id=selected_recipe.rec_id).all()
    db.session.delete(selected_recipe)
    for items in selected_junction:
        db.session.delete(items)
    db.session.commit()
    
    return redirect(url_for('home'))

@app.route('/update_recipe/<rec_id>', methods=['GET','POST'])
def update_recipe(rec_id):
    current_recipe = Cocktailrecipes.query.get(rec_id)
    form = UpdateRecipe()
    aringredients = Ingredient.query.all()
    arquants = Quantity.query.all()

    if request.method == 'POST':
        current_recipe.name = form.name.data
        current_recipe.description = form.description.data
        current_recipe.method = form.method.data
        drop_old_junction = Junction.query.filter_by(rec_id=current_recipe.rec_id).all()
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
        
        db.session.add(new_junction1)
        db.session.add(new_junction2)
        db.session.add(new_junction3)
        db.session.add(new_junction4)
        db.session.add(new_junction5)
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
        form.quants1.choices = [(quantity.quantity_id, quantity.quantity_ml) for quantity in arquants]
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
    dictionary = {}
    selected_recipe = Cocktailrecipes.query.get(rec_id)
    ings_quants = db.session.query(Ingredient,Quantity)\
        .select_from(join(Ingredient, Junction))\
        .join(Cocktailrecipes, Cocktailrecipes.rec_id == Junction.rec_id)\
        .join(Quantity, Quantity.quantity_id == Junction.quantity_id)\
        .filter(Junction.rec_id==selected_recipe.rec_id).all()

    for i, q in ings_quants:
        dictionary[i] = q

    return render_template('details.html', selected_recipe=selected_recipe, dictionary=dictionary)

# @app.route('/search_by_name', methods=['GET','POST'])
# def search():
    
#     return 'name'

# @app.route('/search_by_group', methods=['GET','POST'])
# def search_by_group():
    
#     return 'group'

# @app.route('/search_by_ing', methods=['GET','POST'])
# def search_by_ing():
    
#     return 'ingredient'