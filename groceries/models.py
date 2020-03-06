from django.db import models
from datetime import datetime

class Groceries(models.Model):
  name = models.CharField(max_length=200)
  qty = models.CharField(max_length=200)
  receive_date = models.CharField(max_length=100)
  expiration = models.CharField(max_length=100,blank=True)
  category = models.CharField(max_length=20,blank=True)
  description = models.TextField(blank=True)
  price = models.IntegerField(default=0)
  sale_price = models.IntegerField(default=0,blank=True)
  pro_type = models.CharField(max_length=200)
  is_published = models.BooleanField(default=True)
  date_publish = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.name