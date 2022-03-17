from django.contrib import admin
from .models import Greet

class GreetAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'content_k', 
        'content_h', 
        'content_s', 
        'content_p', 
        'content_m', 
        'content_j', 
        'content_c', 

        )
    search_fields = ('name__user_id',)

admin.site.register(Greet, GreetAdmin)