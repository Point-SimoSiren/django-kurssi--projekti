from django.shortcuts import render
from .models import Supplier, Product

def landingview(request):
    return render (request, "landingpage.html")

def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return render (request, "suppliers.html", context)

def productlistview(request):
    productlist = Product.objects.all()
    context = {'products': productlist}
    return render (request, "products.html", context)
