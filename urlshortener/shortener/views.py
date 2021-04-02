from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Url
from .forms import UrlForm

def shortener(request):
    form = UrlForm()

    if request.method == 'POST':
        form = UrlForm()
        if form.is_valid():
            return HttpResponseRedirect('/Thanks/')

    context = {
        'form':form,
    }

    return render(request, 'shortener/shortener.html', context)