from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Blog, Category
from django.db.models import Q


# Create your views here.
def posts_by_category(request, id):
    # Fetch the post that belongs to the category with the id:id
    posts = Blog.objects.filter(status="Published", category=id)
    print(id,posts)
    # try:
    #     category = Category.objects.get(id=id)
    # except:
    #     # redirect to home
    #     return redirect("home")
    category = get_object_or_404(Category, id=id)
    # use get_object_or_404() to show custom 404 page
    context = {"posts": posts, "category": category}
    return render(request, "post_by_category.html", context)


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status="Published")
    context = {
        "single_blog": single_blog,
    }
    return render(request, "blogs.html", context)

def search(request):
    keyword = request.GET.get("keyword")
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status="Published")
    context = {
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request, "search.html",context)
