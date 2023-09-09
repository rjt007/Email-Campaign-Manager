from django.db import models
import datetime

# Create your models here.

#Subscribers Model
class Subscriber(models.Model):
    first_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)


#Campaign Model
class Campaign(models.Model):
    subject = models.CharField(max_length=100)
    preview_text = models.TextField()
    article_url = models.URLField()
    html_content = models.TextField()
    plain_text_content = models.TextField()
    published_date = models.DateField(default=datetime.date.today)
