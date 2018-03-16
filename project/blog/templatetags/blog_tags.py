from ..models import POST,Category
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
    return Category.objects.all()