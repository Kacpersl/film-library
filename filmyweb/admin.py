from django.contrib import admin
from .models import Film, Writer
# Register your models here.

class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    ordering = ['author']
    list_filter = ('author',)

admin.site.register(Film, FilmAdmin)
admin.site.register(Writer)