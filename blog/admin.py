from django.contrib import admin
from .models import Category, Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ('title', 'content', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on',)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    search_fields = ['title', 'content']
    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'post', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['user', 'body']
