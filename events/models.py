from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Event(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, related_name="project",null=False,on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=300, blank=True,null=True)
    date = models.DateTimeField(blank=True,null=True)
    venue  = models.TextField(max_length=300,blank=True)
    venue_url=models.URLField(blank=True, null=True)
    image_url=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.event_name} | {self.description} | {self.image_url}"

    def __unicode__(self):
        return unicode(self.user)