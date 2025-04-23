from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from posts.models import Post, Tag
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from blog.settings import POST_COUNT_ON_PAGE
from posts.forms import CommentForm

# Create your views here.

# posts = [
#     {
#         "id": 1,
#         "title": "Understanding Django ORM",
#         "content": "Django ORM allows developers to interact with the database easily."
#     },
#     {
#         "id": 2,
#         "title": "Building REST APIs",
#         "content": "Django REST framework is powerful for building web APIs quickly."
#     },
#     {
#         "id": 3,
#         "title": "Handling Authentication",
#         "content": "Django provides built-in support for authentication and authorization."
#     }
# ]

# def helloWorld(request):
#     # return HttpResponse("<html><h1>Hello World!</h1></html>")
#     html = ""
#     for post in posts:
#         html += "<html><div><h1>{} - {}</h1><p>{}</p></div></html>".format(post["id"],post["title"],post["content"])
#     return HttpResponse(html)

def home(request):
   # return HttpResponse("<html><h1>Hello World!</h1></html>")
    # html = ""
    # for post in posts:
    #     html += "<html><div><a href='/post/{}'/><h1>{} - {}</h1></a><p>{}</p></div></html>".format(post["id"], post["id"],post["title"],post["content"])
    # # return HttpResponse(html) 
    # name = "vishal saxena" # For testing & learning
    # # return render(request, 'posts/home.html', {"posts":posts, "name":name})
    # return render(request, 'posts/index.html', {"posts":posts})
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login/')
    else:
        all_posts = Post.objects.all().order_by('-id') # latest post
        paginator = Paginator(all_posts, POST_COUNT_ON_PAGE)
        page_number = request.GET.get('p', 1)
        page_obj = paginator.get_page(page_number)
        # return render(request, 'posts/index.html', {"posts":all_posts})
        return render(request, 'posts/index.html', {"posts":page_obj})
        

def post(request, id):
    # valid_id = False
    # for post in posts:
    #     if post['id'] == id:
    #         html = "<html><div><h1>{} - {}</h1><p>{}</p></div></html>".format(post["id"],post["title"],post["content"])
    #         valid_id = True
    #         break
    # if valid_id:
    #     # return HttpResponse(html)
    #     # return render(request, 'posts/post.html', {"post":post})
    #     return render(request, 'posts/post_tpl.html', {"post":post})
    # else:
    #     # return HttpResponseNotFound("Post not available😉")
    #     raise Http404()
    # try:
    #     post = Post.objects.get(id=id)
    # except:
    #     raise Http404()
    # return render(request, 'posts/post_tpl.html', {"post":post})
    post = get_object_or_404(Post, id=id)
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login/')
    else:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
                return HttpResponseRedirect(reverse('post', args=[id]))
        else:
            form = CommentForm()
            post = get_object_or_404(Post, id=id)
            return render(request, 'posts/post_tpl.html', {"post":post, 'form':form})    
        
    
def google(request, id):
    # return HttpResponseRedirect("https://www.google.com")
    # return HttpResponseRedirect("/post/{}/".format(id))
    url = reverse("post", args=[id])
    return HttpResponseRedirect(url)

def tags(request, id):
    tag = Tag.objects.get(id=id)
    return render(request, 'posts/tags.html', {'tags':tag.post_set.all()})