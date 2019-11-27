from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBlogPostForm, UpdateBlogPostForm
from blog.models import BlogPost
from account.models import Account
# Create your views here.


def create_blog_view(request):

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateBlogPostForm(request.POST or None, request.FILES or None)

    if request.POST:
        if form.is_valid():
            obj = form.save(commit=False)

            author = Account.objects.filter(email=user.email).first()
            obj.author = author
            obj.save()
            form = CreateBlogPostForm()

    context = {
        'form': form
    }
    return render(request, 'blog/create_blog.html', context)


def blog_detail_view(request, slug):
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    blog = get_object_or_404(BlogPost, slug=slug)
    context = {
        'post': blog
    }
    return render(request, 'blog/detail.html', context)


def edit_blog_view(request, slug):
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    context = {}

    blog_post = get_object_or_404(BlogPost, slug=slug)
    if request.POST:
        form = UpdateBlogPostForm(
            request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success'] = True

            blog_post = obj

    form = UpdateBlogPostForm(
        initial={
            "title": blog_post.title,
            "body": blog_post.body,
            "image": blog_post.image
        }
    )

    context['form'] = form

    return render(request, 'blog/edit_blog.html', context)
