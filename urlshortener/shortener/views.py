from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Url

import uuid

def shortener(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse('localhost:8000/'+uid)

    return render(request, 'shortener/shortener.html')

def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)
