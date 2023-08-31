from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Faqs(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.name
