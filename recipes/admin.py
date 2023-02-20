from django.contrib import admin

from .models import Category, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # list_display = (
    #     'title',
    #     'description',
    #     'slug',
    #     'preparation_time',
    #     'preparation_time_unit',
    #     'servings',
    #     'servings_unit',
    #     'preparation_steps',
    #     'preparations_steps_is_html',
    #     'created_at',
    #     'update_at',
    #     'is_published',
    #     'cover',
    #     'category',
    #     'author'
    # )
    ...
