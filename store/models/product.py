from django.db import models
from .category import Category
class Product(models.Model):
    Productname=models.CharField(max_length=100)
    Productprice=models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    Productdescription=models.CharField(max_length=200,default='',null=True,blank=True)
    Productimage=models.ImageField(upload_to='assests/pictures/')

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_product():
        return Product.objects.all()

    @staticmethod
    def get_all_product_by_categoryid(category_id):
        if category_id:
          return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_product()