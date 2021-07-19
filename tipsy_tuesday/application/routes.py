from flask import redirect, request, url_for
from flask.templating import render_template
from application import app, db
from application.models import Cocktailrecipes, Ingredientgroup, Ingredient, Quantity, Junction
from application.forms import AddIngredient


@app.route('/')
def home():
    return render_template(url_for('home'))


@app.route('/add_ingredient', methods=["GET", "POST"])
def add_ingredient():
    form = AddIngredient()
    
    if request.method == 'POST':
        new_ingredient = Ingredient(ing_name=form.ingredient.data, ing_group_id=form.ing_group.data)
        db.session.add(new_ingredient)
        db.session.commit()

        return redirect(url_for('home'))
    
    else:
        ing_groups = Ingredientgroup.query.all()
        form.ing_group.choices = [(ing_groups.ing_group_id, ing_groups.group_name) for ing_group in ing_groups]

        return render_template('add_ingredient.html', form=form)


@app.route('/add_recipe')
def add_recipe():
    return