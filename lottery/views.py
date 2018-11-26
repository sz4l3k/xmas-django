from django.shortcuts import render
from django.http import HttpResponse
import pickle

with open('/home/pi/xmas/lottery/results.txt', 'rb') as f:
    results = pickle.load(f)

def index(request):
    return render(request, 'index.html')

def onlogin(request):
    if request.method == 'POST':
        key = request.POST.get('secret_key', None)
        return render(request, 'response.html', {'name' : results[key]})
    else:
        return render(request, 'index.html')
# Create your views here.
