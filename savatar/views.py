from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    #return render(request, 'savatar/index.html', context=None)
    template = loader.get_template('savatar/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
    #return HttpResponse("<h1>Work bitch!</h1>")
