from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

#should create radio list for on sale, pending, sold
#models.Model means that the Post is a Django model
class Post(models.Model):
    realtor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)   #ForeignKey means link to another model
    address = models.CharField(max_length = 200)                                        #CharField means txt w/limited char
    decription = models.TextField()                                                     #TextField means long text, unlimited
    published_date = models.DateTimeField(blank = True, null = True)                    #DateTimeField is date and time
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.address