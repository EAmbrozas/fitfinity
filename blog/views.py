from django.shortcuts import render
from .models import Category


def home(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'blog/home.html', context)


def category(request, pk):
    category = Category.objects.get(id=pk)
    context = {'category': category}
    return render(request, 'blog/category.html', context)
