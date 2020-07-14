from django.db import models

# Create your models here.
class PasteBinDB(models.Model):
    
    DBManager = models.Manager()
    url = models.CharField(max_length = 264)
    text = models.CharField(max_length = 10000)

    def __str__(self):
        return self.url