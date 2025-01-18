from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment, Category
from .forms import CommentForm, BlogForm


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    # obtain all posts in database
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
            messages.error(
                request,
                "The details you have entered are invalid, please try again."
                )
            return redirect('donate')
        return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }

    return render(request, "blog/detail.html", context)


@login_required
def add_blog(request):
    """ Add a blog post to the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse, ('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added blog post!')
            return redirect(reverse('blog_detail', args=[post.id]))
        else:
            messages.error(
                request,
                'Failed to add the blog post. Please ensure the form is valid.'
                )
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, post_id):
    """ Edit a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse, ('home'))

    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'{post.title} has been updated successfully!'
            )
            return redirect(reverse('blog_detail', args=[post.pk]))
        else:
            messages.error(
                request,
                'Failed to update blog post. Please ensure the form is valid.'
            )
    else:
        form = BlogForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'post': post,
        'post_id': post_id
    }
    return render(request, template, context)


@login_required
def delete_blog(request, post_id):
    """ Delete a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse, ('home'))

    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Blog article deleted!')

    return redirect(reverse('blog_index'))


@login_required
def delete_comment(request, comment_id):
    """ Delete a comment post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse, ('home'))

    comment = get_object_or_404(Comment, pk=comment_id)
    post = comment.post
    comment.delete()
    messages.success(request, 'Comment deleted!')

    return redirect(reverse('blog_detail', args=[post.id]))
