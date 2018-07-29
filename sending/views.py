from django.shortcuts import render
import requests 
import json
from django.shortcuts import redirect, reverse
from .models import Sent, Token
import urllib

token = '-'

NO_PROXY = {
    'no': 'pass',
}

def sending(request):
    sents = Sent.objects.all().order_by('pk')
    return render(request, 'sending/sending.html', {'sents':sents})

def webhook(request):
    url='https://webhook.site/3641365c-6e56-4e4d-80f6-0c4c1f42cc90'
    d={
        'is_active':1,
        'page':0
    }
    r=requests.post(url, data = json.dumps(d), proxies=urllib.getproxies())
    #s = requests.Session(config={'trust_env': False})
    
    al=Sent.objects.create()
    al.json_out = str(d)
    al.uri = url
    al.json_in = r.text
    al.status = r.status_code
    al.save()
    return redirect(reverse('sending'))

def token(request):
    url="https://testirovanieapi.s20.online/v2api/auth/login"
    d={
        'email':'riabozei19@gmail.com',
        'api_key':'bad6583e-9018-11e8-838e-d8cb8abf9305'
    }
    r=requests.post(url, data = json.dumps(d), proxies=urllib.getproxies())
    #s = requests.Session(config={'trust_env': False})
    
    al=Sent.objects.create()
    al.json_out = str(d)
    al.uri = url
    al.json_in = r.text
    al.status = r.status_code
    al.save()
    
    #t=Token.objects.all().delete()
    #t=Token.objects.create()
    #t.code = json.loads(r.text)['token']
    #t.save()
    token = str(json.loads(r.text)['token'])
    
    return redirect(reverse('sending'))

def clear(request):
    Sent.objects.all().delete()
    return redirect(reverse('sending'))

def read(request):

    url="https://testirovanieapi.s20.online/v2api/auth/login"
    d={
        'email':'riabozei19@gmail.com',
        'api_key':'bad6583e-9018-11e8-838e-d8cb8abf9305'
    }
    r=requests.post(url, data = json.dumps(d), proxies=urllib.getproxies())
    #s = requests.Session(config={'trust_env': False})
#    al=Sent.objects.create()
#    al.json_out = str(d)
#    al.uri = url
#    al.json_in = r.text
#    al.status = r.status_code
#    al.save()
    
    #t=Token.objects.all().delete()
    #t=Token.objects.create()
    #t.code = json.loads(r.text)['token']
    #t.save()
    token = json.loads(r.text)['token']

    url="https://testirovanieapi.s20.online/v2api/branch/index"
    d={
        'is_active':1,
        'page':0
    }
    
    headers = {'X-ALFACRM-TOKEN':token}
    r=requests.post(url, data = json.dumps(d), headers = headers, proxies=urllib.getproxies())
    #s = requests.Session(config={'trust_env': False})
    
    al=Sent.objects.create()
    al.json_out = str(d)
    al.uri = url
    al.json_in = r.text
    al.status = r.status_code
    al.save()

    return redirect(reverse('sending'))    


