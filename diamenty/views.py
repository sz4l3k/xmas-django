from django.shortcuts import render
from django.http import HttpResponse

import pickle
import os
from pathlib import Path

home = str(Path.home())

with open(home + '/kacik.txt', 'rb') as f:
    results = pickle.load(f)

def index(request):
    return render(request, 'diamenty/index.html')

def onlogin(request):
    if request.method == 'POST':
        key = request.POST.get('secret_key', None)
        name = results.get(key)
        if name == None:
            return render(request, 'diamenty/error.html', {})
        else:
            return render(request, 'diamenty/response.html', {'name' : name})
    else:
        return render(request, 'diamenty/index.html')
# Create your views here.
