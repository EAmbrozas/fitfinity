from django.shortcuts import render
from .models import Category, Post


def home(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'blog/home.html', context)


def category(request, pk):
    category = Category.objects.get(pk=pk)
    posts = Post.objects.filter(category__pk=pk)
    print(category)
    print(posts)
    context = {'category': category, 'posts': posts}
    return render(request, 'blog/category.html', context)
