from django.shortcuts import render
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImages, Categories, Materials
from django.core.urlresolvers import reverse
from django.views import generic


def index(request):
    latest_product_list = Product.objects.all()[:4]
    all_products = Product.objects.all()
    list_of_all_products = [[product, ProductImages.objects.get(Product=product, MainImage=True)] for product in all_products]
    list_of_products_and_images = [[product, ProductImages.objects.get(Product=product, MainImage=True), ProductImages.objects.filter(Product=product)] for product in latest_product_list]
    context = {'latest_product_list': list_of_products_and_images, 'list_of_all_products': list_of_all_products}
    return render(request, 'polls/index/index.html', context)


def products(request):
    all_products = Product.objects.all()
    all_materials = Materials.objects.all()
    all_categories = Categories.objects.all()
    # list_of_products_and_images = [[product, ProductImages.objects.get(Product=product, MainImage=True),
    #                                 ProductImages.objects.filter(Product=product)] for product in all_products]
    list_of_products_and_images = []
    for product in all_products:
        try:
            list_of_products_and_images.append([product, ProductImages.objects.get(Product=product, MainImage=True),
                                     ProductImages.objects.filter(Product=product)])
        except ProductImages.objects.get(Product=product, MainImage=True).DoesNotExist:
            list_of_products_and_images.append([product, '',
                                                ''])
    list_of_materials = [materials for materials in all_materials]
    list_of_categories = [categories for categories in all_categories]
    context = {'list_of_products_and_images': list_of_products_and_images, 'list_of_materials': list_of_materials,
               'list_of_categories': list_of_categories}
    return render(request, 'polls/products/products.html', context)


def about(request):
    return render(request, 'polls/about/about_page.html')


def login(request):
    return render(request, 'polls/login/login.html')


def basket(request):
    return render(request, 'polls/buy/buy.html')


def about_eng(request):
    return render(request, 'polls/about_eng/about_page.html')

