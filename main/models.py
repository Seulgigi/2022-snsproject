from distutils.command.upload import upload
from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LifePost(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    day = models.DateField()
    image = models.ImageField(upload_to = "post/admin/")
    body = models.CharField(max_length=500)
    # created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "post/all/")
    like_user_set = models.ManyToManyField(User, blank=True, related_name='like_user_set', through='Like')
    dislike_user_set = models.ManyToManyField(User, blank=True, related_name='dislike_user_set', through='DisLike')

    @property
    def like_count(self):
        return self.like_user_set.count()

    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]

class Comment(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post ,on_delete=models.CASCADE, related_name ='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'post'))

class DisLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'post'))