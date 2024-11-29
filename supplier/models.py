from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    company_name = models.CharField(max_length=100)
    location = models.TextField()

    def __str__(self):
        return self.name

class RawMaterial(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='materials')
    name = models.CharField(max_length=100)
    price_per_unit = models.FloatField()
    available_quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.supplier.name}"
