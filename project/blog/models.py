from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField('分类', max_length=20)
    class Meta:
        db_table = 'category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('标签', max_length=20)
    class Meta:
        db_table = 'tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class POST(models.Model):
    title = models.CharField('标题', max_length=30)
    content = models.TextField()
    published_time = models.DateTimeField('发布日期', auto_now_add=True)
    created_time = models.DateTimeField('创建日期', auto_now_add=True)
    category = models.ForeignKey(Category, on_delete='descase')
    tag = models.ManyToManyField(Tag)
    views = models.PositiveIntegerField('浏览量', default=0)
    author = models.ForeignKey(User, on_delete='descase')
    class Meta:
        db_table = 'post'
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['created_time']
    def __str__(self):
        return self.title
    def increase_views(self):
        self.views+=1
        self.save(update_fields=['views'])
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
