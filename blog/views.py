from django.shortcuts import render, HttpResponse, redirect
from .models import Post, BlogComment

# Create your views here.


def blogHome(request):
    allposts = Post.objects.all()
    context = {"allposts": allposts}
    return render(request, "blog/blogHome.html", context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug)[0]
    comments = BlogComment.objects.filter(post=post)
    context = {"post": post, "comments": comments}
    return render(request, "blog/blogPost.html", context)


def postComment(request):
    if request.method == "POST":
        user = request.user
        comment = request.POST.get("comment")
        postSno = request.POST.get("postSno")
        post = Post.objects.get("sno = postSno")
        comment = BlogComment(comment=comment, user=user, post=post)
        comment.save()
        return redirect(f"/blog/{post.slug}")
