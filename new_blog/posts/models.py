from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
