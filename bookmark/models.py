from django.db import models

# Create your models here.
class Bookmark(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.title