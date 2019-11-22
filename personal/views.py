from django.shortcuts import render
from account.models import Account

# Create your views here.


def homeview(request):
    '''
    landing page
    '''
    print(request.headers)

    users = Account.objects.all()
    context = {
        "accounts": users
    }

    return render(request, 'personal/home.html', context)
