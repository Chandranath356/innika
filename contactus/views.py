from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.decorators import method_decorator
from adminfunction.middleware.auth import auth_middleware
from .models import Contactus
from .serializer import ContactusSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['POST'])
def contactuspost(request):
    serializer = ContactusSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({'type':'success','msg':serializer.data})
    else: 
        return Response({'type':'error','msg':serializer.errors})
def index(request):
    contactus = Contactus.objects.all()
    return render(request,'admintemplates/contactus.html',{'contactus':contactus})