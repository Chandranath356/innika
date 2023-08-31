from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=20)
    slug = models.CharField(max_length=20)
    content = RichTextUploadingField(blank=True,null=True)

    def __str__(self):
        return self.name
