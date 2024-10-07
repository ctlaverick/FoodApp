from django.forms import ModelForm, modelformset_factory
from .models import Food, Ingredients, Recipie, Meal, MealPlan

# Form to add and update foods
class AddFoodForm(ModelForm):

    class Meta:
        model = Food
        fields = ['name',]

# Form for the ingredients model
class IngredientsForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = ['user', 'name', 'food', 'amount', 'units']

# Form for Recipies
class RecipiesForm(ModelForm):
    class Meta:
        model = Recipie
        fields = ['name', 'description', 'recipie']

    test = None

IngredientsFormset = modelformset_factory(
    Ingredients, fields=['food', 'amount', 'units'], extra=1
)