from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class POST(models.Model):
    author = models.ForeignKey(User, on_delete='descase')
    title = models.CharField(max_length=20)
    text = models.TextField()
    createdtime = models.DateTimeField(default=timezone.now)
    publishedtime = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.publishedtime = timezone.now()
        self.save()

    def __str__(self):
        return self.title