from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from location.models import Location
from datetime import date
from django.utils import timezone
# Create your models here.
class Properties(models.Model):
    class Status(models.TextChoices):    
        for_sale='for_sale'
        for_rent ='for_rent'
    class Type(models.TextChoices):    
        apartment=1
        vila =2
        flat =3
        rooms =4
        house =5
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    content = RichTextUploadingField(blank=True,null=True)
    short_content = RichTextUploadingField(blank=True,null=True)
    address = models.CharField(max_length=100,blank=True)
    start_form = models.CharField(max_length=100,blank=True)
    top_property = models.BooleanField(default = 0)
    featured = models.BooleanField(default = 0)
    highlight = RichTextUploadingField(blank=True,null=True)              
    location = models.ForeignKey(Location, default=None, on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices =Status.choices,default='for_sale')
    type = models.CharField(max_length=100,choices =Type.choices,default=1)
    # Property Details
    property_id = models.CharField(max_length=100,blank=True)
    price = models.CharField(max_length=100,blank=True)
    property_size = models.CharField(max_length=100,blank=True)
    year_of_bulit = models.DateField(("Date"), default=date.today)
    bedroom = models.CharField(max_length=100,blank=True)
    bathroom = models.CharField(max_length=100,blank=True)
    garage = models.BooleanField(default = 0)
    parking = models.BooleanField(default = 0)
    # Offices Amenities
    balcony = models.BooleanField(default = 0)
    air_conditioning = models.BooleanField(default = 0)
    fireplace = models.BooleanField(default = 0)
    dining_room = models.BooleanField(default = 0)
    basement = models.BooleanField(default = 0)
    cooling = models.BooleanField(default = 0)
    lawn = models.BooleanField(default = 0)
    diswasher = models.BooleanField(default = 0)
    microwave = models.BooleanField(default = 0)
    tv_cable = models.BooleanField(default = 0)
    wifi = models.BooleanField(default = 0)
    refrigerator = models.BooleanField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    

class PropertiesImage(models.Model):
    properties = models.ForeignKey(Properties, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='properties',null=True)
    feature_image = models.BooleanField(default = 0) 