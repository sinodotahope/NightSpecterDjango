from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Group,Tool,Door

admin.site.register(Group)
admin.site.register(Tool)
admin.site.register(Door)