from django.contrib import admin

from .models import desc
class descAdmin(admin.ModelAdmin):
    list_display=('title','description','ak_img')
# Register your models here.

admin.site.register(desc,descAdmin)
