from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=70)
    content = RichTextUploadingField(blank=True,null=True)
    designation = models.CharField(max_length=70,null=True)
    images = models.FileField(upload_to='testimonial',null=True)
    is_featured = models.BooleanField(default = 0)

    def __str__(self):
        return self.name
