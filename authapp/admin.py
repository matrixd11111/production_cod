from django.contrib import admin
from .models import PlayerUser

@admin.register(PlayerUser)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['username', 'slug', 'health']
