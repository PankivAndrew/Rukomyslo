from django.shortcuts import render
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .models import Product,ProductImages
from django.core.urlresolvers import reverse
from django.views import generic


def index(request):
    latest_product_list = Product.objects.all()[:4]
    list_of_products_and_images = [(product, ProductImages.objects.get(Product=product)) for product in latest_product_list]
    context = {'latest_product_list': list_of_products_and_images}
    return render(request, 'polls/index/index.html', context)


def products(request):
    all_products = Product.objects.all()
    list_of_products_and_images = [(product, ProductImages.objects.get(Product=product)) for product in
                                   all_products]
    context = {'all_products': list_of_products_and_images}
    return render(request, 'polls/products/products.html', context)


def about(request):
    return render(request, 'polls/about/about_page.html')


def login(request):
    return render(request, 'polls/login/login.html')
