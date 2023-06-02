from django.contrib import admin
from .models import User, TeamManager
from django.contrib.auth.models import Group

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id', 
        'name', 
        'department',
        'grade',
        'track', 
        'leader',
        'student1',
        'student2',
        'student3',
        )
    search_fields = ('user_id', 'name', 'department')

admin.site.register(User, UserAdmin)
admin.site.unregister(Group) # Admin페이지의 GROUP삭제

class TeamManagerAdmin(admin.ModelAdmin):
    list_display = (
        'tm', 
        'src', 
        'hi',
        'email',
        'department', 
        )
    search_fields = ('tm', )

admin.site.register(TeamManager, TeamManagerAdmin)