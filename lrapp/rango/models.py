# coding: utf-8
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils.text import slugify
from django.template import Library
from django.template.defaultfilters import stringfilter
from django.contrib.auth.models import User

register = Library()


@register.filter(is_safe=True)
@stringfilter
def _slugify(value):
    return slugify(value, allow_unicode=True)


class Category(models.Model):
    owner = models.ForeignKey(User, related_name='categories')
    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = _slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Page(models.Model):
    owner = models.ForeignKey(User, related_name='pages')
    category = models.ForeignKey(Category, related_name='contain_pages')
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
