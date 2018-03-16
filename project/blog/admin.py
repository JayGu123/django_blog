from django.contrib import admin
from .models import *
# Register your models here.
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'published_time', 'created_time',)

admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(POST, PostAdmin)