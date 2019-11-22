from django.shortcuts import render

# Create your views here.


def homeview(request):
    '''
    landing page
    '''
    print(request.headers)
    list_of_values = [
        'first entry',
        'second entry',
        'third entry',
        'forth entry'
    ]
    context = {
        "text": 'This is from context',
        'list': list_of_values
    }

    return render(request, 'personal/home.html', context)
