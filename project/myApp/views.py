from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.aggregates import Count
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from haystack.forms import SearchForm
from .models import *
from .form import *
# Create your views here.

def hello(request):
    posts = POST.objects.all()
    return render(request, 'myApp/hello.html',{'posts' :posts})

def post_detail(request, pk):
    post = get_object_or_404(POST, pk=pk)
    return render(request, 'myApp/post_detail.html', {'post':post})
@login_required
def post_new(request):
    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('/',pk=post.pk)
    else:
        form = postForm()
    return render(request, 'myApp/post_new.html', {'form':form})
@login_required
def post_edit(request, pk):
    post = get_object_or_404(POST, pk=pk)
    if request.method == "POST":
        form = postForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = postForm(instance=post)
    return render(request, 'myApp/post_new.html', {'form': form})

def post_draft_list(request):
    posts = POST.objects.all()
    return render(request, 'myApp/post_draft_list.html', {'posts': posts})
@login_required
def post_publish(request,pk):
    post = get_object_or_404(POST, pk=pk)
    post.publish()
    return redirect('/post/%s' % pk)

def post_remove(request, pk):
    post = get_object_or_404(POST,pk=pk)
    post.delete()
    return redirect('/')

def full_search(request):
    keywords = request.GET['q']
    sform = SearchForm(request.GET)
    posts = sform.search()
    return render(request, 'myApp/post_search_list.html', {'posts':posts, 'list_header':'关键字\'{}\'搜索结果'.format(keywords)})

#def post_list(request):
    #postsAll = POST.objects.annotate(num_comments=Count('comment')).prefetch_related('category').prefetch_related('tags').filter(publishedtime__isnull=False).order_by('publishedtime')
    #for p in postsAll:
        #p.click = cache_manager.get_click(p)