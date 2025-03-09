from django.contrib import admin
from testapp.models import tempmodel
class tempmodeladmin(admin.ModelAdmin):
    list_display = ['name','roll','city','feedbackform']
admin.site.register(tempmodel,tempmodeladmin)