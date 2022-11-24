from django.contrib import admin

from .models import Contact
class contactAdmin(admin.ModelAdmin):
    list_display=('id','name','email','subject','message','date')
# Register your models here.

admin.site.register(Contact,contactAdmin)