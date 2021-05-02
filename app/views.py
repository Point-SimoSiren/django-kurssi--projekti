from django.shortcuts import render,redirect
from .models import Supplier, Product
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User

# LANDING AFTER LOGIN

def landingview(request):
    return render (request, "landingpage.html")

# LOGIN AND LOGOUT

def loginview(request):
    return render (request, "loginpage.html")

def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    user = authenticate(username = user, password = passw)
    if user:
        login(request, user)
        context = {'name': user}
        return render(request,'landingpage.html',context)
    else:
        return render(request, 'loginerror.html')

def logout_action(request):
    logout(request)
    return render(request, 'loginpage.html')

# SUPPLIERS HANDLING AND VIEW FUNCTIONS

def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return render (request,"suppliers.html",context)

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

def edit_supplier_get(request, iidee):
    supplier = Supplier.objects.filter(id = iidee)
    context = {'supplier': supplier}
    return render (request,"edit_supplier.html",context)

def edit_supplier_post(request, iidee):
    item = Supplier.objects.get(id = iidee)
    item.contactname = request.POST['contactname']
    item.address = request.POST['address']
    item.phone = request.POST['phone']
    item.email = request.POST['email']
    item.country = request.POST['country']
    item.save()
    return redirect(supplierlistview)

# PRODUCTS HANDLING AND VIEW FUNCTIONS

def productlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        productlist = Product.objects.all()
        context = {'products': productlist}
        return render(request,"products.html",context)

def addproduct(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        a = request.POST['productname']
        b = request.POST['packagesize']
        c = request.POST['unitprice']
        d = request.POST['unitsinstock']
        e = request.POST['companyname']
        Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, companyname = e).save()
        return redirect(request.META['HTTP_REFERER'])

def deleteproduct(request, iidee):
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

# Get products by company name

def products_filtered(request, iidee):
    supplierObj = Supplier.objects.get(id = iidee)
    cname = supplierObj.companyname
    productlist = Product.objects.all()
    filteredproducts = productlist.filter(companyname = cname)
    context = {'products': filteredproducts}
    return render (request,"products.html",context)
