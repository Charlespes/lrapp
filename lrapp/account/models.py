from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from lrapp.rango.models import Category, Page


class FavCategory(models.Model):
    user = models.OneToOneField(User)
    categories = models.ManyToManyField(Category)
    created_on = models.DateTimeField(auto_now_add=True)


class FavPage(models.Model):
    user = models.OneToOneField(User)
    pages = models.ManyToManyField(Page)
    created_on = models.DateTimeField(auto_now_add=True)
