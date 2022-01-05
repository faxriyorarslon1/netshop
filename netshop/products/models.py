from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name="Kategoriya nomi",max_length=30)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.name        


class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Brend nomi",max_length=30)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brandlar"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="nomi",max_length=30)
    description = models.TextField(verbose_name="haqida")
    price = models.FloatField(verbose_name="narxi")
    image = models.ImageField(verbose_name="surati", upload_to="product_image")
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Maxsulot"
        verbose_name_plural = "Maxsulotlar"

    def __str__(self):
        return self.name+" "+str(self.price)






    
