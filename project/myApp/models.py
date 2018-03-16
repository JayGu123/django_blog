from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=10)
    class Meta:
        db_table = 'tags'
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        db_table = 'categorys'
        verbose_name = '分类'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name

class POST(models.Model):
    author = models.ForeignKey(User, on_delete='descase')
    title = models.CharField(max_length=20)
    text = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True,)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete='descase')
    click = models.IntegerField(default=0)
    createdtime = models.DateTimeField(default=timezone.now)
    publishedtime = models.DateTimeField(blank=True, null=True)
    last_modified_time = models.DateTimeField(auto_now_add=True)
    def publish(self):
        self.publishedtime = timezone.now()
        self.save()
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'posts'
        verbose_name = u'文章'
        verbose_name_plural =verbose_name

class Comment(models.Model):
    blog = models.ForeignKey(POST, verbose_name='文章', on_delete='descase')
    user = models.ForeignKey(User, on_delete='descase')
    content = models.CharField(max_length=250)
    publishedtime = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        db_table = 'comments'
    def __unicode__(self):
        return self.content

