# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from dday.models import Post
from dday.forms import *
# Create your views here.


def index(request):
    posts = Post.objects.all()
    status = Post.objects.first().STATUS_CHOICES
    form = CommentForm()
    return render(request, 'html/index.html', {
        'posts': posts,
        'form': form,
        'status': status,
    })


def comment_new(request, pk):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cmt = form.save(commit=False)
            cmt.post = Post.objects.get(pk=pk)
            cmt.save()
            return redirect(index)
        '/'
    else:
        form = CommentForm()
    return render(request, 'html/index.html', {
        'form': form,
        'posts': posts,
    })


def post_new(request):
    status = Post.objects.first().STATUS_CHOICES
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get()
            post.save()
            return redirect(index)
    else:
        form = PostForm()
    return render(request, 'html/post.html', {
        'form': form,
        'status': status,
    })


def post_edit(request, pk):
    posts = Post.objects.all()
    post = get_object_or_404(Post, pk=pk)
    status = Post.objects.first().STATUS_CHOICES
    # 수정후 sublit 하면 POST로 요청이 옴 아니면 수정전
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = Post.objects.get(pk=pk).author
            post.save()
            return redirect(index)
    else:
        form =PostForm(instance=post)
    return render(request, 'html/post_edit.html', {
        'post': post,
        'posts': posts,
        'editform': form,
        'status': status,
    })
