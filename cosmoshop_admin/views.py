from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")

def profile(request):
    return render(request,"profile.html")

def update_profile(request):
    return render(request,"update-profile.html")

def add_customer(request):
    return render(request,"add-customer.html")
    
def view_customer(request):
    return render(request,"view-customer.html")

def add_supplier(request):
    return render(request,"add-supplier.html")

def view_supplier(request):
    return render(request,"view-supplier.html")

def add_product(request):
    return render(request,"add-product.html")

def view_product(request):
    return render(request,"view-product.html")
