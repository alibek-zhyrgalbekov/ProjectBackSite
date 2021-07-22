from django.contrib import admin

# Register your models here.
from main.models import News, ImageNews, Bookmarks

admin.site.register(News)
admin.site.register(ImageNews)
admin.site.register(Bookmarks)

