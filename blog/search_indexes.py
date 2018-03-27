#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 27, 2018, 11:01 PM
 * Software: PyCharm
 * Project Name: Tutorial
"""

from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(
        document=True,
        use_template=True
    )

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
