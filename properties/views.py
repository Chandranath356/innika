from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from adminfunction.middleware.auth import auth_middleware
from .models import Properties,PropertiesImage
from innika.functions.functions import handle_uploaded_file
from .forms import PropertyForm,PropertyImageForm
from location.models import Location
from django.contrib import messages
# Create your views here.

@auth_middleware
def index(request):
    property = Properties.objects.all()
    return render(request,'admintemplates/properties/index.html',{'properties':property})

def create(request):
    if request.method == 'POST':
        featured_image = request.POST.getlist('feature_image')
        fn = PropertyForm(request.POST)
        files = request.FILES.getlist("image")
        en = PropertyImageForm()
        location = Location.objects.all()
        # print(fn)
        # return HttpResponse(fn)
        if fn.is_valid():
            title = fn.cleaned_data['title']
            slug = fn.cleaned_data['slug']
            content = fn.cleaned_data['content']
            highlight = fn.cleaned_data['highlight']
            location = fn.cleaned_data['location']
            short_content = fn.cleaned_data['short_content']
            address = fn.cleaned_data['address']
            start_form = fn.cleaned_data['start_form']
            top_property = fn.cleaned_data['top_property']
            featured = fn.cleaned_data['featured']
            property_id = fn.cleaned_data['property_id']
            price = fn.cleaned_data['price']
            property_size = fn.cleaned_data['property_size']
            year_of_bulit = fn.cleaned_data['year_of_bulit']
            bedroom = fn.cleaned_data['bedroom']
            bathroom = fn.cleaned_data['bathroom']
            garage = fn.cleaned_data['garage']
            parking = fn.cleaned_data['parking']
            balcony = fn.cleaned_data['balcony']
            air_conditioning = fn.cleaned_data['air_conditioning']
            dining_room = fn.cleaned_data['dining_room']
            basement = fn.cleaned_data['basement']
            cooling = fn.cleaned_data['cooling']
            lawn = fn.cleaned_data['lawn']
            diswasher = fn.cleaned_data['diswasher']
            microwave = fn.cleaned_data['microwave']
            tv_cable = fn.cleaned_data['tv_cable']
            wifi = fn.cleaned_data['wifi']
            refrigerator = fn.cleaned_data['refrigerator']
            if Properties.objects.filter(slug=slug).exists():
                messages.error(request, "Slug is already exists")
                return redirect('/admin/properties/create')
            else:
                ef = Properties(title=title,slug=slug,content=content,highlight=highlight,location=location,
                                short_content=short_content,address=address,top_property=top_property,featured=featured,property_id=property_id,
                                price=price,start_form=start_form,property_size=property_size,year_of_bulit=year_of_bulit,bedroom=bedroom,
                                bathroom=bathroom,garage=garage,parking=parking,balcony=balcony,air_conditioning=air_conditioning,
                                dining_room=dining_room,basement=basement,cooling=cooling,lawn=lawn,
                                diswasher=diswasher,microwave=microwave,tv_cable=tv_cable,wifi=wifi,
                                refrigerator=refrigerator)
                ef.save()
            count = 0
            featured_image_index = 0
            for f in request.FILES.getlist('image'):
                if not featured_image:
                    if(count == 0):
                        featured_image_index = 1
                    else:
                        featured_image_index = 0
                else:
                    if(count == int(featured_image[0])):
                        featured_image_index = 1
                    else:
                        featured_image_index = 0 
                count = count+1
                PropertiesImage.objects.create(properties=ef,images=f,feature_image=featured_image_index)
            return redirect('/admin/properties')
        else:
            return render(request, 'admintemplates/properties/add.html', {'form':fn,'location':location,'imageform':en})
    else:
        fn = PropertyForm()
        en = PropertyImageForm()
        location = Location.objects.all()
        return render(request,'admintemplates/properties/add.html',{'form':fn,'imageform':en,'location':location})
    
def edit(request,propertiesid):
    if(request.user.is_authenticated == False):
        return redirect('/dj-admin')
    else:
        if request.method == 'POST':
            featured_image = request.POST.getlist('feature_image')
            pi = Properties.objects.get(id=propertiesid)
            fn = PropertyForm(request.POST or None,instance = pi)
            en = PropertyImageForm()
            if fn.is_valid():
                if Properties.objects.filter(slug=pi.slug).exclude(id=propertiesid).exists():
                   messages.error(request, "Slug is already exists")
                   return redirect('/admin/properties/edit/'+str(propertiesid))
                else:
                    return HttpResponse(789)
                    fn.save()
                    for f in request.FILES.getlist('image'):
                        PropertiesImage.objects.create(properties=pi,images=f)
                    if featured_image:
                        properties_image = PropertiesImage.objects.all().filter(properties_id=propertiesid)
                        PropertiesImage.objects.all().filter(properties_id=propertiesid).update(feature_image=0)
                        property_images_id = properties_image[int(featured_image[0])].id
                        PropertiesImage.objects.all().filter(id=property_images_id).update(feature_image=1)
                    return redirect('/admin/properties')
        else:
            fn = PropertyForm()
            en = PropertyImageForm()
            location = Location.objects.all()
            properties = Properties.objects.get(id=propertiesid)
            fn=PropertyForm(request.POST or None,instance = properties)
            properties_image = PropertiesImage.objects.all().filter(properties_id=propertiesid)
            total_image = len(properties_image)
        return render(request,'admintemplates/properties/edit.html',{'form':fn,'imageform':en,'location':location,'properties':properties,'form':fn,'properties_image':properties_image,'total_image':total_image})

def delete(request,propertiesid):
    if(request.user.is_authenticated == False):
        return redirect('/dj-admin')
    else:
        PropertiesImage.objects.filter(id=propertiesid).delete();
        return HttpResponse('success')
    
def deleteproperties(request,propertiesid):
    if(request.user.is_authenticated == False):
        return redirect('/dj-admin')
    else:
        location = Properties.objects.get(id=propertiesid)
        location.delete()
        return redirect('/admin/properties')