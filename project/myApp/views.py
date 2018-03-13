from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import POST
from .form import postForm
# Create your views here.

def hello(request):
    posts = POST.objects.all()
    return render(request, 'myApp/hello.html',{'posts' :posts})

def post_detail(request, pk):
    post = get_object_or_404(POST, pk=pk)
    return render(request, 'myApp/post_detail.html', {'post':post})

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

def post_publish(request,pk):
    post = get_object_or_404(POST, pk=pk)
    post.publish()
    return redirect('/post/%s' % pk)

def post_remove(request, pk):
    post = get_object_or_404(POST,pk=pk)
    post.delete()
    return redirect('/')

def post_list(request):
    postsAll = POST.objects.filter(publishedtime__isnull=False).order_by('publishedtime')