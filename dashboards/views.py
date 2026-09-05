from django.shortcuts import render
from blogs.models import Category, Blog


# Create your views here.
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {
        "category_count": category_count,
        "blogs_count": blogs_count
    }
    # print(categories, blogs)
    return render(request, "dashboard/dashboard.html", context)
