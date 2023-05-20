from django.db import models

class Category(models.Model):
    Categoryname=models.CharField(max_length=200)


    @staticmethod
    def get_all_categories():
        return Category.objects.all()


    def __str__(self):
        return self.Categoryname