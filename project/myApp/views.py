from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import POST
# Create your views here.

def hello(request):
    posts = POST.objects.all()
    return render(request, 'myApp/hello.html',{'post' :posts})