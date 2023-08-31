from django.db import models

# Create your models here.
# Create your models here.
class Menu(models.Model):
    menu_id = models.IntegerField()
    name = models.CharField(max_length=70)
    slug = models.CharField(max_length=70,null=True)
    parent_id = models.IntegerField()
    
    def __str__(self):
        return self.name
