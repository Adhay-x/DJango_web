from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Products
# Create your views here.

@login_required(login_url='login')
def home(request):
    my_product = Products.objects.all()
    product = {
        'pro': my_product
        }  
    return render(request, 'index.html', product)



