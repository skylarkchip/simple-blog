from django.shortcuts import render
from account.models import Account

# Create your views here.


def home_screen_view(request):
    template = 'personal/home.html'
    
    # 1st way to add into context
    context = {}
    # context['some_string'] = 'Some string passed from an object'

    # 2nd way to add into context
    """
    context = {
        'some_string': 'Some string passed from an object'
    }

    list_of_values = []
    list_of_values.append('First Entry')
    list_of_values.append('Second Entry')
    list_of_values.append('Third Entry')
    list_of_values.append('Fourth Entry')

    context['list_of_values'] = list_of_values
    """
    accounts = Account.objects.all()
    context['accounts'] = accounts

    return render(request, 'personal/home.html', context)
