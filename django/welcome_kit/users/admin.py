from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id', 
        'name', 
        'modifier',
        'department',
        'grade',
        'track', 
        'leader',
        'value',
        'interest',
        'student1',
        'student1_intro',
        'student2',
        'student2_intro'
        )
    search_fields = ('user_id', 'name', 'department')

admin.site.register(User, UserAdmin)
admin.site.unregister(Group) # Admin페이지의 GROUP삭제
