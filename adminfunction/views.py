from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.utils.decorators import method_decorator
from adminfunction.middleware.auth import auth_middleware
from django.urls import reverse_lazy
from .forms import PasswordChangingForm
from location.models import Location
from properties.models import Properties
from contactus.models import Contactus
# Create your views here.
def admin_login(request):
    
    try:
        if request.user.is_authenticated:
            return redirect('/admin/dashboard')
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.error(request,'Account not found')
                return redirect('/dj-admin')
            else:
                user_obj = authenticate(username=username,password=password)
                if user_obj and user_obj.is_superuser:
                    login(request,user_obj)
                    return redirect('/admin/dashboard')
                else:
                    messages.error(request,'Invalid Password')
                    return redirect('/dj-admin')
        
        return render(request,'adminfunction/login.html')
    
    except Exception as e:
        print(e)

@auth_middleware
def dashboard(request):
    location = Location.objects.count()
    properties = Properties.objects.count()
    contactus = Contactus.objects.count()
    return render(request,'admintemplates/dashboard.html',{'location':location,'properties':properties,'contactus':contactus})

@auth_middleware
def handlelogout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('/dj-admin')

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('change_password')

def password_success(request):
    return render(request)
 


