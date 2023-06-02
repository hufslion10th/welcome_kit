from .models import Greet
from django.contrib import admin

class GreetAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        
        'kim', 
        'one', 
        'min', 
        'cho',
        'win',
        'yes', 
        'cwj', 
        'kyk', 
        'sim',
        'cha',
        'hye',
        'kye',

        )
    search_fields = ('name__user_id',)

admin.site.register(Greet, GreetAdmin)