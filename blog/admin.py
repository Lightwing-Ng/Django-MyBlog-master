#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 27, 2018, 7:15 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""

from django.contrib import admin
from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'created_time',
        'modified_time',
        'category',
        'author'
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
