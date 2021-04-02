from django.shortcuts import render
from django.http import HttpResponse

from .models import Url

import uuid

def shortener(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)

    return render(request, 'shortener/shortener.html')

