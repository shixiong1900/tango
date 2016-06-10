from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage': 'Crunchy, creay, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'myname': 'gaoXiang'}
    return render(request, 'rango/about.html', context=context_dict)

