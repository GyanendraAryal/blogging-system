from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Blog, Category, Comment
from django.db.models import Q


# Create your views here.
def posts_by_category(request, id):
    # Fetch the post that belongs to the category with the id:id
    posts = Blog.objects.filter(status="Published", category=id)
    print(id, posts)
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
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST["comment"]
        comment.save()
        return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(blog=single_blog)
    comments_count = comments.count()
    context = {
        "single_blog": single_blog,
        "comments": comments,
        "comments_count": comments_count,
    }
    return render(request, "blogs.html", context)


def search(request):
    keyword = request.GET.get("keyword")
    blogs = Blog.objects.filter(
        Q(title__icontains=keyword)
        | Q(short_description__icontains=keyword)
        | Q(blog_body__icontains=keyword),
        status="Published",
    )
    context = {"blogs": blogs, "keyword": keyword}
    return render(request, "search.html", context)
