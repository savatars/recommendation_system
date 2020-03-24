from django.db import models
from django.conf import settings
# Create your models here.
class features(models.Model):
		customerId=models.CharField(max_length=7, default='0000000', editable=False)
		recommendedProducts=models.TextField(default='-')
		def __str__(self):
			return self.customerId