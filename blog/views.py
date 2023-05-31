from django.shortcuts import render


categories = [
    {'id': 1, 'Title': 'All about training'},
    {'id': 2, 'Title': 'All about exercises'},
    {'id': 3, 'Title': 'All about diet'},
]


def home(request):
    context = {'categories': categories}
    return render(request, 'blog/home.html', context)


def category(request, pk):
    category = None
    for i in categories:
        if i['id'] == int(pk):
            category = i
    context = {'category': category}
    return render(request, 'blog/category.html', context)
