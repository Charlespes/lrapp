from django.contrib import admin

from .models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'slug')
    exclude = ('owner',)
    prepopulated_fields = {'slug': ('name',)}

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
        obj.save()


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'owner')
    exclude = ('owner', 'category')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
        obj.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
