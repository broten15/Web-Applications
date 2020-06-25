from django.contrib import admin

# Register your models here.

from meal_plans.models import Day, Meal

admin.site.register(Day)
admin.site.register(Meal)
