from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
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
        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        return context
    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range
        if page_number == 1:
            right = page_range[page_number:page_number+2]
            if right[-1] < total_pages-1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page_number == total_pages:
            left = page_range[(page_number-3) if (page_number-3)>0 else 0 : page_number-1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page_number-3) if (page_number-3)>0 else 0:page_number-1]
            right = page_range[page_number:page_number+2]
            if right[-1] < total_pages-1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
            if left[0]>2:
                left_has_more = True
            if left[0]>1:
                first = True
        data = {
            'left':left,
            'right':right,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'firt':first,
            'last':last,

        }
        return data

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
                                             'markdown.extensions.toc',
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
                                     extensions = [
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post':post,
        'form':form,
        'comment_list':comment_list,
    }
    return render(request, 'blog/single.html', context)

class ArchivesView(IndexView):
    model = POST
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year, created_time__month=month, created_time__day=True)


class CategoryView(IndexView):
    model = POST
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)

class TagView(IndexView):
    model = POST
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tag=tag)

class SearchView(IndexView):
    model = POST
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    def get_context_data(self):
        context = super(SearchView, self).get_context_data()
        error_message = ''
        if not q:
            error_message = '请输入关键字'
        data = {
            'error_message':error_message,
        }
        context.update(data)
        return context
    def get_queryset(self):
        q = self.kwargs.get('q')
        return super(SearchView,self).get_queryset().filter(Q(title__icontains=q)|Q(content__icontais=q))

def search(request):
    q = request.GET.get('q')
    error_message = ''
    if not q:
        error_message = '请输入关键字'
        return render(request, 'blog/index.html', {'error_message':error_message})
    posts = POST.objects.filter(Q(title__icontains=q)|Q(content__icontains=q))
    return render(request, 'blog/index.html', {'posts':posts, 'error_message':error_message})