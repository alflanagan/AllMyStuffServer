from django.contrib import admin

# Register your models here.
from .models import Category, TextNote

admin.site.register(TextNote)
admin.site.register(Category)
