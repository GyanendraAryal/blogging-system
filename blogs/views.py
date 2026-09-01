from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Blog, Category


# Create your views here.
def posts_by_category(request, id):
    # Fetch the post that belongs to the category with the id:id
    posts = Blog.objects.filter(status="Published", category=id)
    # try:
    #     category = Category.objects.get(id=id)
    # except:
    #     # redirect to home
    #     return redirect("home")
    category = get_object_or_404(Category, id=id)
    # use get_object_or_404() to show custom 404 page
    context = {
        "posts": posts,
        "category": category
        }
    return render(request, "post_by_category.html", context)
