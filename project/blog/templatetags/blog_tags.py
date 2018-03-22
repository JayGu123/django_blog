from ..models import POST,Category,Tag
from django.db.models.aggregates import Count
from django import template


register = template.Library()
@register.simple_tag
def get_recent_list(num=5):
    return POST.objects.all().order_by('created_time')[:num]

@register.simple_tag
def archives():
    return POST.objects.dates('created_time','month',order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts = Count('post')).filter(num_posts__gt=0)


@register.simple_tag
def get_tags():
    return Tag.objects.all()