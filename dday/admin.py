# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from dday.models import Post, Comment
from django import forms
# Register your models here.


class Postadmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'name', 'start', 'finish')


admin.site.register(Post, Postadmin)
admin.site.register(Comment)
