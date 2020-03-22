from django.db import models
from datetime import datetime
from pastors.models import pastor
class Listing(models.Model):
    pastor=models.ForeignKey(pastor,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200)
    duration=models.CharField(max_length=200)
    location=models.CharField(max_length=100)
    verse=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    audio_size=models.IntegerField()
    video_size=models.IntegerField()
    video_1 = models.FileField(upload_to='videos/%Y/%m/%d/',blank=True)
    audio_1 = models.FileField(upload_to='audios/%Y/%m/%d/',blank=True)
    textfile_1 = models.FileField(upload_to='textfiles/%Y/%m/%d/',blank=True)
   
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=False)
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_4=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_5=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_6=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    is_published=models.BooleanField(default=True)
    list_date=models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title
 
    