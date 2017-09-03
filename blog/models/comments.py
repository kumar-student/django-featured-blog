from django.db import models
from django.conf import settings
from blog.models.articles import Article

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False)
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comment')
    comment = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.timestamp

    def __str__(self):
        return self.timestamp