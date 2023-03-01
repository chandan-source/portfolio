from django.shortcuts import render
from django.shortcuts import redirect
from.models import *

# Create your views here.
def home(request):
    return render(request,'base.html')
def aboutus(request):
    return render(request,'about.html')
def my_work(request):
    return render(request,'work.html')
def blog(request,bid):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')