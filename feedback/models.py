from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User

class Feedback(models.Model):
    REQUEST_MAX_LEN = 2048
	
    site = models.ForeignKey(Site)
    url = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    text = models.TextField()
    
    user = models.ForeignKey(User, blank=True, null=True)
    request = models.TextField(max_length=REQUEST_MAX_LEN)
    
    created = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=[(0, 'new'), (1, 'old')], default=0)

    class Meta:
        ordering = ["-created"]

    def __unicode__(self):
        return u'%s: %s: %s' % (self.created, self.url, self.subject)

