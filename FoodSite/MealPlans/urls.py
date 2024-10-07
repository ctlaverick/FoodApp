from django.contrib.auth import views as auth_views
from django.urls import path
from . import views as mp_views

urlpatterns = [
    path('home/', mp_views.PortalHome, name="portal_home"),
    path('view/food', mp_views.view_food, name="view_food"),
    path('add/food', mp_views.add_food, name="add_food"),
    path('delete/food/<int:food_id>/', mp_views.delete_food, name="delete_food"),
    path('update/food/<int:food_id>/', mp_views.update_food, name="update_food"),
    path('view/ingredients', mp_views.view_ingredients, name="view_ingredients"),
    path('view/recipies', mp_views.view_recipies, name="view_recipies"),
    path('add/ingredients', mp_views.add_ingredient, name="add_ingredient"),
    path('add/recipie', mp_views.add_recipie, name="add_recipie"),
    path('formset', mp_views.ingredients_formset_test, name="ingredients_formset_test"),
]