from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    check_box = models.BooleanField(null=True)
    multiple_check_box = models.CharField(max_length=255, null=True)
    pulldown = models.CharField(max_length=255, null=True)
    radio = models.CharField(max_length=255, null=True)