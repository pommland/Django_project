# from django.http import HttpResponse
from django.shortcuts import render

from .models import Product

# Create your views here.
def product_datail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title':obj.title,
    #     'description':obj.description
    # }
    context ={
        "object" : obj
    }
    return render(request,"product/detail.html",context)