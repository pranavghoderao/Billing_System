from django.db import models

# Create your models here.
class CustomerDetails(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    panNo = models.CharField(max_length=10)
    Gstin = models.CharField(max_length=20)
    
    class Meta:
        db_table = "customerdetails"


class ProductInfo(models.Model):
    prodName = models.CharField(max_length=100)
    prodCode = models.CharField(max_length=20)

    class Meta:
        db_table = "productinfo"

class InvoiceNO(models.Model):
    billno = models.IntegerField()
    
    class Meta:
        db_table = "invoiceno"
        