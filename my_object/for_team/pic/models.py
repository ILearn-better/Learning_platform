from django.db import models

class picture(models.Model):
    # name = models.CharField(max_length=50,blank=True, null=True)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.photo.name
# Create your models here.
