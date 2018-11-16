from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

#should create radio list for on sale, pending, sold
#models.Model means that the Post is a Django model
class Post(models.Model):
    realtor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)   #ForeignKey means link to another model
    address = models.CharField(max_length = 200)                                        #CharField means txt w/limited char
    description = models.TextField()                                                     #TextField means long text, unlimited
    published_date = models.DateTimeField(blank = True, null = True)                    #DateTimeField is date and time
    
    onsale = 'On Sale'
    contract_pending = 'Contract Pending'
    sold = 'Sold'
    sell_choices = (
        (onsale, 'onsale'),
        (contract_pending, 'contract_pending'),
        (sold, 'sold'),
    )
    
    seller = models.CharField(max_length = 16, choices = sell_choices, default = onsale)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.address
    
    
#messages if interested in house
class Comment(models.Model):
    post = models.ForeignKey('realestate.Post', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)   #EmailField is similar to CharField but uses an email validator
    text = models.TextField()
    sent_date = models.DateTimeField(default=timezone.now)
    
    def seen(self):
        self.save()
        
    def __str__(self):
        return self.text