from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from adminfunction.middleware.auth import auth_middleware
from .forms import FaqsForm
from .models import Faqs
# Create your views here.
@auth_middleware
def faqs(request):
    loc = Faqs.objects.all()
    return render(request,'admintemplates/faqs/index.html',{'location':loc})

@auth_middleware
def addfaqs(request):
    if request.method == 'POST':
        fn = FaqsForm(request.POST)  
        if fn.is_valid():
            accoradation_title = fn.cleaned_data['title']
            accoradation_desc = fn.cleaned_data['content']
            en = Faqs(title=accoradation_title,content=accoradation_desc)
            en.save()
            return redirect('/admin/faqs')
        # else:
            # return render(request, 'admintemplates/addlocation.html', {'form':fn})
    else:
        fn=FaqsForm()
    return render(request,'admintemplates/faqs/add.html',{'form':fn})

def editfaqs(request,faqsid):
    if(request.user.is_authenticated == False):
        return redirect('/dj-admin')
    else:
        pi = Faqs.objects.get(id=faqsid)
        fn=FaqsForm(request.POST or None,instance = pi)
        if request.method == 'POST':
            if fn.is_valid():
                fn.save()
                return redirect('/admin/faqs')
            else:
                return render(request,'admintemplates/faqs/edit.html',{'form':fn})
        else:
            return render(request,'admintemplates/faqs/edit.html',{'form':fn})
        
def deletefaqs(request,faqsid):

    if(request.user.is_authenticated == False):
        return redirect('/dj-admin')
    else:
        location = Faqs.objects.get(id=faqsid)
        location.delete()
        return redirect('/admin/faqs')