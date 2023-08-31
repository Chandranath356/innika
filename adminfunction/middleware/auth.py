from django.views.decorators.common import no_append_slash
from django.shortcuts import render,redirect
from django.http import HttpResponsePermanentRedirect,HttpResponse
@no_append_slash
def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request,*args,**kwargs):
        
        user = request.user
        if user.is_authenticated== False:
            return redirect('/dj-admin')
           
        return get_response(request)
        
        
    return middleware
