from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category, Blog
from aboutus.models import About, SocialLink

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
