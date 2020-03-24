from django.db import models
from django.conf import settings
# Create your models here.
class features(models.Model):
		timestamp= models.DateTimeField(auto_now_add=True)
		visitorid= models.CharField(max_length=10)
		event=models.CharField(max_length=10)
		itemid=models.CharField(max_length=15)
		def __str__(self):
			return self.visitorid