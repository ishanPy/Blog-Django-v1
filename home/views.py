from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Contact
from django.contrib import messages
from myapp.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, "home/home.html", context)

def about(request):
    messages.success(request,"Welcome to About page")
    return render(request, "home/about.html")
    
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)

        if len(name)<3 or len(email)<3 or len(phone)<10 or len(content)<5:
            messages.error(request, "Please fill the form as correctly")

        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been sent succesfully")

    return render(request, "home/contact.html")

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)

    if allPosts.count() == 0:
        messages.warning(request, "Please enter a valid query")

    context = {'allPosts':allPosts, 'query':query}
    return render(request, "home/search.html", context)

def signup(request):
    if request.method == "POST":
        # get post params
        username1 = request.POST['username']
        pass1 = request.POST['pass1']
        fname = request.POST['fname']
        email = request.POST['email']
        pass2 = request.POST['pass2']

        if len(username1) > 12:
            messages.error(request, "Please choose a username less than 12 characters")
            return redirect("/")

        if not username1.isalnum():
            messages.error(request, "Please choose a username that is alphanumeric.")
            return redirect("/")

        if not "@" in email:
            messages.error(request, "Please enter a valid email")
            return redirect("/")

        if pass1 != pass2:
            messages.error(request, "Your confirmation password didn't match")
            return redirect("/")    
                  
        # checks
        user = User.objects.create_user(username1, email, pass1)
        user.save()
        messages.success(request, "Your superblog account has been created !")
        return redirect("/")

    else:
        return HttpResponse("406 - Not allowed")

def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Hurray ! You are logged in as "+loginusername)
            return redirect("/")

        else:
            messages.error(request, "Sorry, You entered wrong credentials")
            return redirect("/")

def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("/")

    return HttpResponse("handlelogout")

