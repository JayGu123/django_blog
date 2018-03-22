from django.contrib.syndication.views import Feed
from .models import POST

class AllowPostsRss(Feed):
    title = "Jay Gu's blog"
    link = '/'
    description = 'Jay Gu 博客'
    def items(self):
        return POST.objects.all()
    def item_title(self, item):
        return '[%s]%s' % (item.category, item.title)
    def item_description(self, item):
        return item.content