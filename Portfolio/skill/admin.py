from django.contrib import admin
from .models import skill
class skillAdmin(admin.ModelAdmin):
    list_display=('skill_name','skill_percentage')
# Register your models here.

admin.site.register(skill,skillAdmin)