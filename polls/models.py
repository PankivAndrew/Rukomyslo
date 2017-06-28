from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    CategoryID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class Product(models.Model):
    ProductID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=200)
    Price = models.DecimalField(max_digits=10,decimal_places=5)
    Description = models.TextField()
    Quantity = models.IntegerField()
    Address = models.CharField(max_length=200)
    Category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class ProductContactPerson(models.Model):
    PersonID = models.IntegerField()
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ContactPerson = models.CharField(max_length=100)
    Phone1 = models.CharField(max_length=13)
    Phone2 = models.CharField(max_length=13)

    def __str__(self):
        return self.ContactPerson


class ProductImages(models.Model):
    ImageID = models.IntegerField()
    Image = models.ImageField()
    NameOfImage = models.CharField(max_length=50)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.NameOfImage


class Customer(models.Model):
    CustomerID = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User)
    PhoneNumber = models.CharField(max_length=13)

    def __str__(self):
        return self.Nick


class Order(models.Model):
    OrderID = models.IntegerField(primary_key=True)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    OrderTotalPrice = models.DecimalField(max_digits=10,decimal_places=5)
    OrderDate = models.DateField()
    OrderDetails = models.TextField()

    def __str__(self):
        return self.OrderID


class OrderProduct(models.Model):
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    Order_ProductID = models.IntegerField
    ProductQuantity = models.IntegerField
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10,decimal_places=5)
    Description = models.TextField()
    IsDeleted = models.BinaryField()

    def __str__(self):
        return self.Name


class Materials(models.Model):
    MaterialsID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class MaterialsProduct(models.Model):
    Materials = models.ForeignKey(Materials, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    LocalID = models.IntegerField()

    def __str__(self):
        return self.LocalID
