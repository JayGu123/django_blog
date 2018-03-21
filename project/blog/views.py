from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from comments.forms import CommentForm
from .models import *
import markdown
# Create your views here.

class IndexView(ListView):
    model = POST
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        pass

def index(request):
    posts = POST.objects.all().order_by('created_time')
    return render(request, 'blog/index.html', {'posts':posts})

class PostDetailView(DetailView):
    mdoel = POST
    template_name = 'blog/single.html'
    context_object_name = 'post'
    def get(self, request, *args, **kwargs):
        response = super(PostDetailView,self).get(request, *args, **kwargs)
        print(self.object.name)
        self.object.increase_views()
        return response
    def get_object(self,queryset=None):
        post =super(PostDetailView, self).get_object(queryset=None)
        post.content = markdown.markdown(post.content,
                                         extensions = [
                                             'markdown.extensions.extra',
                                             'markdown.extensions.codehilite',
                                             'markdown.extensions,toc',
                                         ])
        return post
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form':form,
            'comment_lsit':comment_list,
        })
        return context

def detail(request, pk):
    post = get_object_or_404(POST, pk=pk)
    post.increase_views()
    post.content = markdown.markdown(post.content,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc'
                                     ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post':post,
        'form':form,
        'comment_list':comment_list,
    }
    return render(request, 'blog/single.html', context)

class ArchivesView(ListView):
    model = POST
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year, created_time__month=month, created_time__day=True)

def archives(request, year, month):
    posts = POST.objects.filter(created_time__year=year, created_time__month=month, created_time__day=True).order_by('created_time')
    return render(request, 'blog/index.html', {'posts':posts})

class CategoryView(ListView):
    model = POST
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)

def categories(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    posts = POST.objects.filter(category=cate).order_by('created_time')
    return render(request, 'blog/index.html', {'posts':posts})
