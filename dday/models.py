# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    STATUS_CHOICES = (
        ('success', '육군'),
        ('primary', '해군'),
        ('info', '공군'),
        ('danger', '해병대'),
    )

    author = models.ForeignKey('auth.user')
    name = models.CharField(max_length=5)
    text = models.TextField()
    start = models.DateField(default=timezone.now)
    finish = models.DateField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='army')

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=10)
    msg = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.msg
