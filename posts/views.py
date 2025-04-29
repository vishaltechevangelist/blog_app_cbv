from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from posts.models import Post, Tag
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from blog.settings import POST_COUNT_ON_PAGE
from posts.forms import CommentForm
from django.db.models import Q
from django.views.generic import ListView, DetailView


def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login/')
    else:
        all_posts = Post.objects.all().order_by('-id') # latest post
        paginator = Paginator(all_posts, POST_COUNT_ON_PAGE)
        page_number = request.GET.get('p', 1)
        page_obj = paginator.get_page(page_number)
        # return render(request, 'posts/index.html', {"posts":all_posts})
        return render(request, 'posts/index.html', {"posts":page_obj})
        
class HomeView(ListView):
    model = Post
    template_name = 'posts/index.html'
    ordering = '-id'
    context_object_name = 'posts'


def post(request, id):
    post = get_object_or_404(Post, id=id)
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login/')
    else:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.user = request.user
                comment.save()
                return HttpResponseRedirect(reverse('post', args=[id]))
        else:
            form = CommentForm()
            post = get_object_or_404(Post, id=id)
            return render(request, 'posts/post_tpl.html', {"post":post, 'form':form, 'comments':post.comment_set.all()})    

class PostView(DetailView):
    model = Post
    template_name = 'posts/post_tpl.html'
    context_object_name = 'post'
    ordering = '-id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comment_set.all().order_by('-id')
        return context
    
    def post(self, request, pk):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(reverse('post', kwargs={'pk': pk}))
    
def google(request, id):
    url = reverse("post", args=[id])
    return HttpResponseRedirect(url)

def tags(request, id):
    tag = Tag.objects.get(id=id)
    return render(request, 'posts/tags.html', {'tags':tag.post_set.all()})

def search(request):
    query = request.GET.get('query', None)
    posts = Post.objects.filter(Q(post_title__icontains=query) | 
                                    Q(post_content__icontains=query)).order_by('-id')
    paginator = Paginator(posts, POST_COUNT_ON_PAGE)
    page_number = request.GET.get('p', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/search.html', {'posts':page_obj, 'query':query})

class SearchView(ListView):
    model = Post
    template_name = 'posts/search.html'
    context_object_name = 'posts'

    def get_queryset(self, request):
        query = request.GET.get('query', None)
        posts = Post.objects.filter(Q(post_title__icontains=query) | 
                                    Q(post_content__icontains=query)).order_by('-id')
        return posts
