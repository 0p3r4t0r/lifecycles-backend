from django.contrib import admin
from .models import Exercise, Set, Workout


@admin.register(Exercise)
class ExercseAdmin(admin.ModelAdmin):
    pass


@admin.register(Set)
class Set(admin.ModelAdmin):
    pass


@admin.register(Workout)
class Workout(admin.ModelAdmin):
    pass