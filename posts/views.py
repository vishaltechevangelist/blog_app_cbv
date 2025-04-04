from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

posts = [
    {
        "id": 1,
        "title": "Understanding Django ORM",
        "content": "Django ORM allows developers to interact with the database easily."
    },
    {
        "id": 2,
        "title": "Building REST APIs",
        "content": "Django REST framework is powerful for building web APIs quickly."
    },
    {
        "id": 3,
        "title": "Handling Authentication",
        "content": "Django provides built-in support for authentication and authorization."
    }
]


def helloWorld(request):
    # return HttpResponse("<html><h1>Hello World!</h1></html>")
    html = ""
    for post in posts:
        html += "<html><div><h1>{} - {}</h1><p>{}</p></div></html>".format(post["id"],post["title"],post["content"])
    return HttpResponse(html)

def home(request):
    # return HttpResponse("<html><h1>Hello World!</h1></html>")
    html = ""
    for post in posts:
        html += "<html><div><a href='/post/{}'/><h1>{} - {}</h1></a><p>{}</p></div></html>".format(post["id"], post["id"],post["title"],post["content"])
    # return HttpResponse(html)
    name = "vishal saxena" # For testing & learning
    # return render(request, 'posts/home.html', {"posts":posts, "name":name})
    return render(request, 'posts/index.html', {"posts":posts, "name":name})

def post(request, id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            html = "<html><div><h1>{} - {}</h1><p>{}</p></div></html>".format(post["id"],post["title"],post["content"])
            valid_id = True
            break
    if valid_id:
        # return HttpResponse(html)
        # return render(request, 'posts/post.html', {"post":post})
        return render(request, 'posts/post_tpl.html', {"post":post})
    else:
        return HttpResponseNotFound("Post not available😉")
    
def google(request, id):
    # return HttpResponseRedirect("https://www.google.com")
    # return HttpResponseRedirect("/post/{}/".format(id))
    url = reverse("post", args=[id])
    return HttpResponseRedirect(url)

    