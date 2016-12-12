# coding: utf-8
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Page(models.Model):
    owner = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.CharField(max_length=128)
    likes = models.IntegerField(default=0)
    desc = models.TextField(max_length=None)

    def __unicode__(self):
        return self.title

    def clean(self):
        for page in self.category.page_set.all():
            if not self.id and page.title == self.title:
                raise ValidationError({'title': _(u'容器下链接标题已存在,请修改标题')})
