from django.contrib import admin
from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "active", "position")
    list_filter = (['active'])
    search_filed = ('title','slug')
    prepopulated_fields = {'slug':('title',)}
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title" ,"category" ,"publish" ,"status")
    list_filter = ('publish','status')
    prepopulated_fields = {'slug':('title',)}
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)