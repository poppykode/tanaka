from django.shortcuts import render
from .models import Post

def home(request):
    template_name = "home.html"
    posts = Post.objects.all()
    context ={
        'posts':posts,
    }
    return render(request,template_name,context)

def post_details(request):
    template_name = "post_details.html"
    posts = ''
    context ={
       
    }
    return render(request,template_name,context)


def about_us(request):
    template_name = "about.html"
    print(request)
    data={
        "company":"Glen View Study centre",
        "address":"10626 Glen View 8"
        }
    return render(request,template_name,data)  
