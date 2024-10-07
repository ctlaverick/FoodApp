from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self) -> str:
        return self.name

class Ingredients(models.Model):
    UNITS_OF_MEASUREMENT = [
        ("Teaspoon", "tsp"),
        ("Tablespoon", "tbsp"),
        ("cup", "cup"),
        ("grams", "g"),
        ("milliliters", "ml"),
    ]


    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=False, blank=False)
    food = models.ForeignKey(to=Food, on_delete=models.CASCADE) # check the delete
    amount = models.FloatField()
    units = models.CharField(max_length=11, choices=UNITS_OF_MEASUREMENT) # check max length
    
    def __str__(self) -> str:
        return self.name

class Recipie(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=False, blank=False)
    description = models.TextField(null=True, blank=False) # check this
    ingredients = models.ManyToManyField(Ingredients)
    recipie = models.TextField(null=False, blank=False)

class Meal(models.Model):
    MEAL_CHOICES= [
        ("BR", "Breakfast"),
        ("LN", "Lunch"),
        ("DN", "Dinner"),
        ("SN", "Snack"),
    ]
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=False, blank=False)
    description = models.TextField(null=True, blank=False) # check this
    type = models.CharField(max_length=2, choices=MEAL_CHOICES)
    recipie = models.OneToOneField("MealPlans.Recipie", on_delete=models.CASCADE) #related name?


class MealPlan(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(unique=True, null=False, blank=False)
    meals = models.ManyToManyField(Meal)