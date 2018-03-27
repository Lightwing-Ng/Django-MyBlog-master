#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Mar 27, 2018, 7:22 AM
 * Software: PyCharm
 * Project Name: Tutorial
"""
import markdown
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
from django.utils.html import strip_tags


@python_2_unicode_compatible
class Category(models.Model):
    """
    Django requires all the models inherited from models.Model
    Refer files:
    https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Tag(models.Model):
    """
    Tag is identical to the Category
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):
    """
    Database of articles
    """
    title = models.CharField(max_length=70)

    # For the article text, usging TextField
    body = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200, blank=True)

    # Recording the reading capacity
    views = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bolg:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        # if the abstract isn't filled
        if not self.excerpt:
            md = markdown.Markdown(
                extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                ]
            )
            self.excerpt = strip_tags(
                md.convert(self.body)[:54]
            )

        # Call the method from the parent class, saving the
        # data to the database
        super(Post, self).save(*args, **kwargs)
