from django.shortcuts import render, redirect
from account.models import Account
from blog.models import BlogPost

# Create your views here.


def homeview(request):
    '''
    landing page
    '''
    print(request.headers)
    user = request.user
    if user.is_authenticated:
        blogs = BlogPost.objects.filter(author=user)
        context = {
            'blogs': blogs
        }
        return render(request, 'personal/home.html', context)
    else:
        return redirect('login')
