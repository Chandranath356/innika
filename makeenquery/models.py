from django.db import models

# Create your models here.
# Create your models here.
class Makeenquery(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=70)
    location = models.CharField(max_length=70)
    comments = models.CharField(max_length=200)

    def __str__(self):
        return self.name
