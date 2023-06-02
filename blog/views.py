from django.shortcuts import render
from .models import Category, Post, Comment


def home(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'blog/home.html', context)


def category(request, pk):
    category = Category.objects.get(pk=pk)
    posts = Post.objects.filter(category__pk=pk)
    context = {'category': category, 'posts': posts}
    return render(request, 'blog/category.html', context)


def post(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post__pk=pk)
    context = {'post': post, 'comments': comments}
    return render(request, 'blog/post.html', context)


def comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    context = {'comment': comment}
    return render(request, 'blog/post.html', context)
