from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=10)

class Category(models.Model):
    name = models.CharField(max_length=20)

class POST(models.Model):
    author = models.ForeignKey(User, on_delete='descase')
    title = models.CharField(max_length=20)
    text = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, on_delete='descase')
    click = models.IntegerField(default=0)
    createdtime = models.DateTimeField(default=timezone.now)
    publishedtime = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.publishedtime = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'posts'
        verbose_name = u'文章'
        verbose_name_plural = u'文章'


