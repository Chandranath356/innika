from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Makeenquery
from .serializer import MakeenquerySerializer

# Create your views here.
@api_view(['POST'])
def addmakeenquery(request):
    serializer = MakeenquerySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'type':'success','msg':serializer.data})
    else: 
        return Response({'type':'error','msg':serializer.errors})
def index(request):
    enquery = Makeenquery.objects.all()
    return render(request,'admintemplates/enquery.html',{'enquery':enquery})