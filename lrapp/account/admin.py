from django.contrib import admin

from .models import FavCategory, FavPage


class FavCategoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_on')

admin.site.register(FavCategory, FavCategoryAdmin)
admin.site.register(FavPage)
