from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

def upload_location(instance, filename):
    return "%s/%s" % (instance.title, filename)

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    file = models.FileField(upload_to=upload_location,null=True,blank=True)
    highlight = models.CharField(max_length=255,null=True,blank=True)
    publish_date = models.DateField(auto_now=False,auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:article-detail", kwargs={"id": self.id})

    class Meta:
        ordering = ['-timestamp', '-updated']