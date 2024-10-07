from django.shortcuts import render, redirect
from .models import Food, Ingredients, Recipie, Meal, MealPlan
from .forms import AddFoodForm, IngredientsForm, RecipiesForm, IngredientsFormset

# Create your views here.
def PortalHome(request):#
    context = {
        "Title": "Portal Home"
    }
    return render(request, 'MealPlans/portal-home.html', context)

def meal_plan_overview(request):
    context = {

    }
    return render(request, 'MealPlans/overview', context)

def add_food(request):
    if request.method == "POST":
        form = AddFoodForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('view_food')
    else:
        form = AddFoodForm

    context = {
        "Title": "Add Food",
        "form": form,
    }
    return render(request, 'MealPlans/add_food.html', context)

def view_food(request):
    foods = Food.objects.filter(user=request.user)
    
    context = {
        'foods': foods,
    }

    return render(request, 'MealPlans/view_foods.html', context=context)

def delete_food(request, food_id):
    food = Food.objects.get(id=food_id)
    if food.user == request.user:
        food.delete()
    return redirect('view_food')

def update_food(request, food_id):
    food = Food.objects.get(id=food_id)

    if request.method == 'POST':
        form = AddFoodForm(request.POST, instance=food)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('view_food')
    else:
        form = AddFoodForm(instance=food)

    context = {
        'form': form,
    }

    return render(request, 'MealPlans/update_food.html', context=context)

# Creating meals
# requires both ingredients and recipe models
# custom form to 

def view_ingredients(request):
    ingredients = Ingredients.objects.filter(user=request.user)

    context = {
        'ingredients': ingredients,
    }

    return render(request, 'MealPlans/view_ingredients.html', context=context)

def add_ingredient(request):
    if request.method == "POST":
        form = IngredientsForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('view_food')
    else:
        form = IngredientsForm

    context = {
        "Title": "Add Ingredient",
        "form": form,
    }
    return render(request, 'MealPlans/add_ingredient.html', context)


def add_recipie(request):
    if request.method == "POST":
        formset = IngredientsFormset(data=request.POST)
        recipie_form = RecipiesForm(request.POST)
        ingredients = []
        if formset.is_valid() and recipie_form.is_valid():
            for form in formset:
                form.instance.name = form.instance.food.name
                form.instance.user = request.user
                form.save()
                ingredients.append(form.instance.id)

            recipie_form.instance.user = request.user
            recipie_form.save()
            recipie_object = Recipie.objects.get(id=recipie_form.instance.id)
            for ingredient_id in ingredients:
                ingredient = Ingredients.objects.get(id=ingredient_id)
                recipie_object.ingredients.add(ingredient)

            return redirect('view_food')
    else:
        recipie_form = RecipiesForm
        ingredients_formset = IngredientsFormset(queryset=Ingredients.objects.none())


    context = {
        "Title": "Add Recipie",
        "recipie_form": recipie_form,
        "ingredients_formset": ingredients_formset,
    }
    return render(request, 'MealPlans/add_recipie.html', context)

def view_recipies(request):
    recipies = Recipie.objects.filter(user=request.user)
    return render(request, 'MealPlans/view_recipies.html', context={'recipies': recipies,})


def ingredients_formset_test(request):
    if request.method == 'POST':
        formset = IngredientsFormset(data=request.POST)
        if formset.is_valid():
            for form in formset:
                form.instance.name = form.instance.food.name
                form.instance.user = request.user
                form.save()
                print(form.instance.id)
            return redirect('view_ingredients')
    else:
        formset = IngredientsFormset(queryset=Ingredients.objects.none())
    return render(request, 'MealPlans/formset.html', context={'formset': formset})
