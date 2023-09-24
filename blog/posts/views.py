from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib import messages

def home(request):
    template_name = "home.html"
    posts = Post.objects.all()
    # posts = Post.objects.all().filter(is_active = True)
    number_of_posts = posts.count()
    number_of_posts_=len(posts)
    context ={
        'posts':posts,
        'number_of_posts': number_of_posts
    }
    return render(request,template_name,context)

def post_details(request, id):
    template_name = "post_details.html"
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post,id=id)
    print("post >>>>>>>>>")
    print(post)
    context ={
        'post':post  
    }
    return render(request,template_name,context)

def create_post(request):
    template_name = 'create_post.html'
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        savePost = Post.objects.create(
            title= title,
            image = image,
            description = description
        )
        print(savePost.id)
        messages.success(request,"Post was successfully created.")
        return redirect('posts:home')



    return render(request,template_name)

def about_us(request):
    template_name = "x/about.html"
    print(request)
    data={
        "company":"Glen View Study centre",
        "address":"10626 Glen View 8"
        }
    return render(request,template_name,data)  
