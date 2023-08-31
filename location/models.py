from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Location(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=200)
    images = models.FileField(upload_to='locations',null=True)
    top_property = models.BooleanField(default = 0)

    def __str__(self):
        return self.name