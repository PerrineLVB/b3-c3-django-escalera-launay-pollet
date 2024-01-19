from django.db import models
from django.urls import reverse
# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    site_url = models.URLField(blank=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('site_details', args=[str(self.id)])
