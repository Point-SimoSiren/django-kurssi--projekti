from django.shortcuts import render, redirect
from .models import Supplier, Product

def landingview(request):
    return render (request, "landingpage.html")

def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return render (request, "suppliers.html", context)


def addsupplier(request):
    a = request.POST['companyname']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])


def deletesupplier(request,iidee):
    Supplier.objects.filter(id = iidee).delete()
    return redirect(request.META['HTTP_REFERER'])


# PRODUCTS HANDLING AND VIEW FUNCTIONS

def productlistview(request):
    productlist = Product.objects.all()
    context = {'products': productlist}
    return render (request, "products.html", context)

def addproduct(request):
    a = request.POST['productname']
    b = request.POST['packagesize']
    c = request.POST['unitprice']
    d = request.POST['unitsinstock']
    e = request.POST['companyname']
    Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, companyname = e).save()
    return redirect(request.META['HTTP_REFERER'])

def deleteproduct(request,iidee):
    Product.objects.filter(id = iidee).delete()
    return redirect(request.META['HTTP_REFERER'])

def edit_product_get(request, iidee):
    product = Product.objects.filter(id = iidee)
    context = {'product': product}
    return render (request,"edit_product.html",context)

def edit_product_post(request, iidee):
    item = Product.objects.get(id = iidee)
    item.unitprice = request.POST['unitprice']
    item.unitsinstock = request.POST['unitsinstock']
    item.save()
    return redirect(productlistview)
