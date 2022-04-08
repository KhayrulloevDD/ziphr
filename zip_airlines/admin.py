from django.contrib import admin
from .models import User, Airplane


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    ordering = ['id']


@admin.register(Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    list_display = ('id', 'passengers', 'capacity', 'consumption_per_minute', 'able_to_fly')
    ordering = ['id']
