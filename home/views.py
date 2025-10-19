from django.shortcuts import render,HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post

# Create your views here.
def home(request):
    return render(request, 'home/home.html')
    

def about(request):
    
    return render(request,'home/about.html')

def contact(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name,email,phone,content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or  len(content)<4:       
            messages.error(request, "please fill form again")

        else:
            contact = Contact(name=name,email=email,phone = phone,content=content,)
            contact.save()
            messages.success(request,"your form has been sucessfully submitted")

    return render(request,'home/contact.html')

def search(request):
    query = request.GET['query']

    if len(query)> 78:
        allPosts= Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains = query)
        allPostContent = Post.objects.filter(content__icontains = query)
        allPosts = allPostsTitle.union(allPostContent)

    if allPosts.count() == 0 :
        messages.warning(request, "no search found please refine your query")


    params = {'allPosts': allPosts , 'query':query }
    return render(request,'home/search.html',params)
    
    

