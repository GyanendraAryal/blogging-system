from django.http import HttpResponse
from django.shortcuts import render,redirect
from blogs.models import Category, Blog
from aboutus.models import About, SocialLink
from .forms import RegisterationForm

def home(request):
    # categories = Category.objects.all()
    try:
        about = About.objects.get()
    except:
        about = None
    # social = SocialLink.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status="Published").order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False, status="Published")
    context = {
               "featured_posts": featured_posts,
               "posts":posts,
               "about":about,
            #    "social":social
               }
    return render(request, "home.html", context)


def register(request):
    if request.method == "POST":
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("register")
    else:
        print(form.errors)

    context ={
        "form":form
    }
    return render(request, 'register.html', context)

def login(request):
    return render(request, "login.html")
