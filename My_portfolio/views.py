from django.shortcuts import render
from django.shortcuts import redirect
from.models import *

# Create your views here.
def home(request):
    all_work=Work.objects.all()
    all_work=all_work[::-1]
    l_work=all_work[:4]
    d={"l_work":l_work}
    return render(request,'base.html',d)
def aboutus(request):
    return render(request,'about.html')
def my_work(request,type):
    wdata=Work.objects.all()
    d={"wdata":wdata,"type":type}
    return render(request,'work.html',d)
def blog(request):
    blogdata=Blog.objects.all()
    d={"blogdata":blogdata}
    return render(request,'blog.html',d)
def contact(request):
    return render(request,'contact.html')