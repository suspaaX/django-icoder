from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length=130)
    time = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title
# Create your models here.

class BlogComment(models.Model):
    sno = models.AutoField(primary_key  = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE )
    timeStamp = models.DateTimeField(default=now)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
  



