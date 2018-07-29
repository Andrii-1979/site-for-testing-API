from django.shortcuts import render
from django.shortcuts import redirect, reverse
from .models import Receive
from django.http import HttpRequest
import json

def receiving(request):
    receives = Receive.objects.all().order_by('pk')
    return render(request, 'receiving/receiving.html', {'receives':receives})
    
def alfa(request):
    al = Receive.objects.create()
    al.method_in = request.method#request.method
    al.host_in = request.get_host()#request.host()
    if request.GET:
        al.json_in = str(json.loads(request.GET))
    elif request.POST:
        al.json_in = str(json.loads(request.POST))
    else:
        al.json_in = '-'#request.json()
    al.date_in = request.scheme#request.scheme#request.data()
    
    al.save()
    return redirect(reverse('receiving'))

def clear(request):
    Receive.objects.all().delete()
    return redirect(reverse('receiving'))
    