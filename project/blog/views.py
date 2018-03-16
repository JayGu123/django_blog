from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
import markdown
# Create your views here.

def index(request):
    posts = POST.objects.all().order_by('created_time')
    return render(request, 'blog/index.html', {'posts':posts})

def detail(request, pk):
    post = get_object_or_404(POST, pk=pk)
    post.content = markdown.markdown(post.content,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc'
                                     ])
    return render(request, 'blog/single.html', {'post':post})

def archives(request, year, month):
    posts = POST.objects.filter(created_time__year=year, created_time__month=month, created_time__day=True).order_by('created_time')
    return render(request, 'blog/index.html', {'posts':posts})

def categories(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    posts = POST.objects.filter(category=cate).order_by('created_time')
    return render(request, 'blog/index.html', {'posts':posts})
