from django.contrib import admin
from .model import Room

@admin.register(Room)
class Room(admin.ModelAdmin):
    list_display = ['room_number','pictures', 'number_of_bed', 'cost', 'description','status'] 
