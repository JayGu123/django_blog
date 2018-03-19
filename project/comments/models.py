from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField('用户名', max_length=100)
    email = models.EmailField('邮箱', max_length=100)
    text = models.TextField('评论内容')
    created_time = models.DateTimeField('评论时间', auto_now_add=True)
    post = models.ForeignKey('blog.POST', on_delete='descase')

    def __str__(self):
        return self.text[:20]
    class Meta:
        db_table = 'comments'
        verbose_name = '评论'
        verbose_name_plural = verbose_name
