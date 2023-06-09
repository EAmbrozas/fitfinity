from django.shortcuts import render, redirect
from .models import Category, Post, Comment
from .forms import CommentForm


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

    if request.method == 'POST':
        comment = Comment.objects.create(
            user=request.user,
            post=post,
            body=request.POST.get('body')
        )
        return redirect('post', pk=post.pk)
    context = {'post': post, 'comments': comments}
    return render(request, 'blog/post.html', context)


def comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    context = {'comment': comment}
    return render(request, 'blog/post.html', context)


def updateComment(request, pk):
    comment = Comment.objects.get(id=pk)
    form = CommentForm(instance=comment)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'blog/update.html', context)


def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('home')
    return render(request, 'blog/delete.html', {'obj': comment})
