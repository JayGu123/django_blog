from django.contrib import admin
from .models import *

# Register your models here.
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
class POSTAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'publishedtime', 'category',)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'user', 'content', 'publishedtime',)




admin.site.register(POST,POSTAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Comment,CommentAdmin)