from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.decorators import method_decorator
from adminfunction.middleware.auth import auth_middleware
from .forms import LocationForm
from .models import Location

# Create your views here.
@auth_middleware
def location(request):
    loc = Location.objects.all()
    return render(request,'admintemplates/locations.html',{'location':loc})

@auth_middleware
def addlocation(request):
    if request.method == 'POST':
        fn = LocationForm(request.POST,request.FILES)
        if fn.is_valid():
            location_name = fn.cleaned_data['title']
            location_desc = fn.cleaned_data['description']
            image = fn.cleaned_data['images']
            en = Location(title=location_name,description=location_desc,images=image)
            en.save()
            return redirect('/admin/location')
        # else:
            # return render(request, 'admintemplates/addlocation.html', {'form':fn})
    else:
        fn=LocationForm()
    return render(request,'admintemplates/addlocation.html',{'form':fn})

def deletelocation(request,locationid):

    if(request.user.is_authenticated == False):
        return redirect('/dj-admin')
    else:
        location = Location.objects.get(id=locationid)
        location.delete()
        return redirect('/admin/location')

def editlocation(request,locationid):

    if(request.user.is_authenticated == False):
        return redirect('/dj-admin')
    else:
        pi = Location.objects.get(id=locationid)
        fn=LocationForm(request.POST or None,request.FILES or None,instance = pi)
        if request.method == 'POST':
            if fn.is_valid():
                fn.save()
                return redirect('/admin/location')
            else:
                
                return render(request,'admintemplates/editlocation.html',{'form':fn})
        else:
            return render(request,'admintemplates/editlocation.html',{'form':fn})