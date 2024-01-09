from django.db import models
# Create your models here.
class Sites(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    site_url = models.URLField(blank=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name
