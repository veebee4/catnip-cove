from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .models import Post, Comment, Category
from .forms import CommentForm, BlogForm


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on") #obtain all posts in database
    context = {
        "posts": posts,
    }
    return render(request, "blog/blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
        else: 
            messages.error(request, "The details you have entered are invalid, please try again.")
            return redirect('donate')
        return HttpResponseRedirect(request.path_info)
        
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }

    return render(request, "blog/detail.html", context)


def add_blog(request):
    """ Add a blog post to the blog """
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added blog post!')
            return redirect(reverse('add_blog'))
        else:
            messages.error(request, 'Failed to add the post. Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)