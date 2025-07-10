from django.contrib import admin
from .models import Author, Post, Tag, Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'tags', 'date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email_name', 'post')

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)