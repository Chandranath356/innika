from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from location.models import Location
from page.models import Page
from properties.models import Properties,PropertiesImage
from django.db.models import Q
from django.db.models import Count
from testimonial.models import Testimonial
# Create your views here.
def index(request,pageslug):
    page = Page.objects.filter(slug=pageslug).all()
    # print(page[0].content)
    return render(request,'frontend/page.html',{'page':page[0]})
def home(request):
    loc = Location.objects.all().filter(top_property=1).annotate(properties_count=Count('properties'))
    property = PropertiesImage.objects.select_related('properties').filter((Q(feature_image=1))).filter(Q(properties__top_property=1))
    return render(request,'frontend/home.html',{'location':loc,'property':property})
def location(request):
    return HttpResponse('location56')
def properties(request):
    location_serch = request.GET.get('loc')
    type_serch = request.GET.get('type')
    status_serch = request.GET.get('status')
    q_search = request.GET.get('q')
    location = Location.objects.all()
    filter_query = Q()
    if location_serch:
        filter_query.add(Q(properties__location=location_serch), Q.AND)
    if type_serch:
        filter_query.add(Q(properties__type=type_serch), Q.AND)
    if status_serch:
        filter_query.add(Q(properties__status=status_serch), Q.AND)
    if q_search:
        filter_query.add(Q(properties__title__icontains=q_search), Q.AND)
    properties = PropertiesImage.objects.select_related('properties').filter((Q(feature_image=1))).filter(filter_query).all()
    return render(request,'frontend/property.html',{'properties':properties,'location':location})
def property_details(request,slug):
    property_details = Properties.objects.filter(slug=slug).prefetch_related('propertiesimage_set').all()
    properties_image = property_details[0].propertiesimage_set.all()
    feature_image = ''
    for x in properties_image:
        if x.feature_image == 1:
            feature_image = x.images
    return render(request,'frontend/propertydetails.html',{'property_details':property_details[0],'properties_image':properties_image,'feature_image':feature_image})
def testimonial(request):
    testimonial = Testimonial.objects.all()
    return render(request,'frontend/testimonial.html',{'testimonial':testimonial})
def faqs(request):
    return render(request,'frontend/faqs.html')
def makeenquery(request):
    return render(request,'frontend/enquery.html')