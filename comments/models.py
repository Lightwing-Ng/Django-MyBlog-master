#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 28, 2018, 1:52 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""

from django.db import models
from django.utils.six import python_2_unicode_compatible


# This decrator is using to compatible with python2
@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]
