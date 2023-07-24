from django.db import models

# Create your models here.

class Item(models.Model):
    def __str__(self):
        return self.item_name
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.ImageField(upload_to="food/images",default="")
    item_shopName = models.CharField(max_length=200,default="")
    item_shopAddress = models.CharField(max_length=200,default="")
    item_discountOffer = models.CharField(max_length=200,default="")
    item_userRole = models.CharField(max_length=200,default="")