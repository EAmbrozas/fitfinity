from django.shortcuts import render


categories = [
    {'id': 1, 'Title': 'All about training'},
    {'id': 2, 'Title': 'All about exercises'},
    {'id': 3, 'Title': 'All about diet'},
]


def home(request):
    context = {'categories': categories}
    return render(request, 'home.html', context)


def category(request):
    context = {'categories': categories}
    return render(request, 'category.html', context)