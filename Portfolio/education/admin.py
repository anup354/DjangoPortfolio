from django.contrib import admin

from education.models import study_detail
class studyAdmin(admin.ModelAdmin):
    list_display=('institution','study_program','start_date','end_date')
# Register your models here.

admin.site.register(study_detail,studyAdmin)