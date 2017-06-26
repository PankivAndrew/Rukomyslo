from django.db import models
from django import forms


class Product(models.Model):
    ProductID = models.IntegerField()
    Name = models.CharField(max_length=200)
    Price = models.DecimalField()
    Description = models.TextField()
    Quantity = models.IntegerField()
    Address = models.CharField(max_length=200)
    CategoryID = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Categories(models.Model):
    CategoryID = models.IntegerField()
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class ProductContactPerson(models.Model):
    PersonID = models.IntegerField()
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    ContactPerson = models.CharField(max_length=100)
    Phone1 = models.CharField(max_length=13)
    Phone2 = models.CharField(max_length=13)

    def __str__(self):
        return self.ContactPerson


class ProductImages(models.Model):
    ImageID = models.IntegerField()
    Image = models.ImageField
    NameOfImage = models.CharField(50)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.NameOfImage


class Customer(models.Model):
    CustomerID = models.IntegerField()
    Nick = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=13)
    Password = models.CharField(widget=forms.PasswordInput)

    def __str__(self):
        return self.Nick


class Order(models.Model):
    OrderID = models.IntegerField()
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    OrderTotalPrice = models.DecimalField()
    OrderDate = models.DateField()
    OrderDetails = models.TextField()

    def __str__(self):
        return self.OrderID


class OrderProduct(models.Model):
    OrderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    Order_ProductID = models.IntegerField
    ProductQuantity = models.IntegerField
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Price = models.DecimalField()
    Description = models.TextField()
    IsDeleted = models.BinaryField()

    def __str__(self):
        return self.Name


class Materials(models.Model):
    MaterialsID = models.IntegerField
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class MaterialsProduct(models.Model):
    MaterialsID = models.ForeignKey(Materials, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    ID = models.IntegerField()

    def __str__(self):
        return self.ID
