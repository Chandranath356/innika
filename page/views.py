from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from adminfunction.middleware.auth import auth_middleware
from .forms import PageForm
from .models import Page
from django.contrib import messages
# Create your views here.
@auth_middleware
def page(request):
    page = Page.objects.all()
    return render(request,'admintemplates/page/allpage.html',{'page':page})

@auth_middleware
def addpage(request):
    fn=PageForm()
    if request.method == 'POST':
        fn = PageForm(request.POST)  
        if fn.is_valid():
            page_title = fn.cleaned_data['title']
            page_slug = fn.cleaned_data['slug']
            page_content = fn.cleaned_data['content']
            if Page.objects.filter(slug=page_slug).exists():
                messages.error(request, "Slug is already exists")
                return redirect('/admin/addpage')
            else:
                en = Page(title=page_title,slug=page_slug,content=page_content)
                en.save()
                return redirect('/admin/page')
    return render(request,'admintemplates/page/addpage.html',{'form':fn})

def editpage(request,pageid):
    
    if(request.user.is_authenticated == False):
        return redirect('/dj-admin')
    else:
        pi = Page.objects.get(id=pageid)
        fn=PageForm(request.POST or None,instance = pi)
        if request.method == 'POST':
            if fn.is_valid():
                fn.save()
                return redirect('/admin/page')
            else:
                return render(request,'admintemplates/page/editpage.html',{'form':fn})
        else:
            return render(request,'admintemplates/page/editpage.html',{'form':fn})

def view(request,product):
    return HttpResponse(456)