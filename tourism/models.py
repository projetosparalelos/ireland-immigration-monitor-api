from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    web = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='places-image')
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
