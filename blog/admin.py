# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from blog.models.articles import Article
from blog.models.comments import Comment
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','highlight','user']
    list_filter = ['title','description','publish_date']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','comment','user','timestamp']
    list_filter = ['comment','user']

admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)