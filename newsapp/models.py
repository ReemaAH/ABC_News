import datetime
from django.db import models
from django.utils import timezone


class News(models.Model):
    ## every news page details will contain these info
    popular = models.BooleanField(default=False)
    category = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    news_image = models.ImageField(upload_to = "images/", blank=True, null=True)
    content_short =  models.CharField(max_length=300)
    content_long = models.CharField(max_length=3000)
   
    def __str__(self):
         return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    