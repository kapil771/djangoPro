from django.contrib import admin
from causes.models import Causes

class CausesAdmin(admin.ModelAdmin):
    list_display=("image","title","description")

admin.site.register(Causes, CausesAdmin)
# Register your models here.