from django.contrib import admin
from .models import Product,Categories,ProductContactPerson,ProductImages,Customer,Order,OrderProduct,Materials,MaterialsProduct
# Register your models here.
admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(ProductContactPerson)
admin.site.register(ProductImages)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Materials)
admin.site.register(MaterialsProduct)