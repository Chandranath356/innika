from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from adminfunction.middleware.auth import auth_middleware
from page.models import Page
from location.models import Location
from properties.models import Properties
from menu.models import Menu
import json
from django.db.models import CharField,Value,IntegerField
from django.http import JsonResponse
# from django.utils import simplejson
# Create your views here.

@auth_middleware
def menu(request):
    if request.method == 'POST':
        menu = request.POST.get('menudata')
        menu1 = json.loads(menu)
        if len(menu1)>0:
            Menu.objects.all().delete()
            for m in menu1:
                en = Menu(menu_id=m["id"],name=m["name"],parent_id=m["parent_id"],slug=m['slug'])
                en.save()
            return JsonResponse({'type':'success','message':'Menu has been created successfully','icon':'bx bx-check-circle'})
        else:
            return JsonResponse({'type':'error','message':'Please update the menu','icon':'bx bx-x-circle'})
    else:
        page = Page.objects.all()
        location = Location.objects.all()
        properties = Properties.objects.all()
        menu = Menu.objects.all().values()
        menumodified = []
        for mf in menu:
            mf['submenu'] = []
            if mf['parent_id'] == 0:
                mf['submenu'] = []
                menumodified.append(mf)
            else:
                menu[mf['parent_id']-1]['submenu'].append(mf)
        return render(request,'admintemplates/menu/index.html',{'page':page,'location':location,'properties':properties,'menu':menumodified})

def index(request,pageslug):
    return HttpResponse(pageslug)
def home(request):
    return HttpResponse('home')
def location(request):
    return HttpResponse('location56')