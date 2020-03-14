from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog_page(request):
    blogs = Blog.objects
    return render(request,"Blog.html",{"blogs":blogs})