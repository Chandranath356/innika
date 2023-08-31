from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from adminfunction.middleware.auth import auth_middleware
from django.contrib import messages
from .models import Testimonial
from .forms import TestimonialForm
# Create your views here.

@auth_middleware
def index(request):
    testimonial = Testimonial.objects.all()
    return render(request,'admintemplates/testimonial/index.html',{'testimonial':testimonial})

@auth_middleware
def add(request):
    fn=TestimonialForm()
    if request.method == 'POST':
        fn = TestimonialForm(request.POST,request.FILES)  
        if fn.is_valid():
            testimonial_title = fn.cleaned_data['name']
            testimonial_description = fn.cleaned_data['content']
            testimonial_designation = fn.cleaned_data['designation']
            image = fn.cleaned_data['images']
            en = Testimonial(name=testimonial_title,content=testimonial_description,images=image,designation=testimonial_designation)
            en.save()
            return redirect('/admin/testimonial')
    return render(request,'admintemplates/testimonial/add.html',{'form':fn})

def edit(request,testimonialid):
    
    if(request.user.is_authenticated == False):
        return redirect('/dj-admin')
    else:
        pi = Testimonial.objects.get(id=testimonialid)
        fn=TestimonialForm(request.POST or None,instance = pi)
        if request.method == 'POST':
            if fn.is_valid():
                fn.save()
                return redirect('/admin/testimonial')
            else:
                return render(request,'admintemplates/testimonial/edit.html',{'form':fn})
        else:
            return render(request,'admintemplates/testimonial/edit.html',{'form':fn})

def delete(request,testimonialid):
    if(request.user.is_authenticated == False):
        return redirect('/dj-admin')
    else:
        testimonial = Testimonial.objects.get(id=testimonialid)
        testimonial.delete()
        return redirect('/admin/testimonial')