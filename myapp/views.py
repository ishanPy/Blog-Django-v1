from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Post, Comment
from django.contrib import messages


def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, "blog/blogHome.html", context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(post=post)
    context = {'post':post, 'comments':comments}
    return render(request, "blog/blogPost.html", context)

def postComment(request):
    if request.method == 'POST':
        comments = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        comments = Comment(comments=comments, user=user, post=post)
        comments.save()
        messages.success(request, "Your comment has been posted")
    
    return redirect(f"/blog/{post.slug}")
