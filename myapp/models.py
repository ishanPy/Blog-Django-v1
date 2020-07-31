from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Post(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=20)
    content = models.TextField()
    slug = models.CharField(max_length=125)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + " by " + self.author
    
class Comment(models.Model):
    sno = models.AutoField(primary_key=True)
    comments = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comments[0:10] + "..."  + " From " + self.user.username
    