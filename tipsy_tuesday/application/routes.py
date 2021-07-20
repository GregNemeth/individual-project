
from flask import redirect, request, url_for
from flask.templating import render_template
from application import app, db
from application.models import Cocktailrecipes, Ingredientgroup, Ingredient, Quantity, Junction
from application.forms import AddGroup, AddIngredient, AddRecipe, Ingreds


@app.route('/')
def home():
    groups = Ingredientgroup.query.all()
    ingredients = Ingredient.query.all()

    return render_template('home.html', groups=groups, ingredients=ingredients)


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


@app.route('/add_recipe')
def add_recipe():
    form = AddRecipe()
    form2 = Ingreds()
    aringredients = Ingredient.query.all()
    arquants = Quantity.query.all()
    
    if request.method == 'POST':
        new_recipe = Cocktailrecipes(name=form.name.data)
        new_recipe.description = form.description.data
        new_recipe.method = form.method.data
        db.session.add(new_recipe)
        db.session.commit()
        
        return(redirect(url_for('home')))

    else:
        
        form2.ingredient.choices = [(ingred.ing_id, ingred.ing_name)for ingred in aringredients]
        form2.quantity.choices = [(quant.quantity_id, quant.quantity_ml)for quant in arquants]
        

        return render_template('add_recipe.html', form=form, form2=form2)
        

    
