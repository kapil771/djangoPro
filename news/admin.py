from django.contrib import admin
from news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display=('title','description')

admin.site.register(News,NewsAdmin)
# Register your models here.