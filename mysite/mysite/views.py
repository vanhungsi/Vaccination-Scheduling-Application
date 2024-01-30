from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'message': 'Hello Django Developer!'
    }
    return render(request, 'mysite/index.html', context)
