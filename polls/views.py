from django.shortcuts import render
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .models import Product
from django.core.urlresolvers import reverse
from django.views import generic



class IndexView(generic.ListView):
    template_name = 'Home page/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Product.objects.order_by('-pub_date')[:5]
