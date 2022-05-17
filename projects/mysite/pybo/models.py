from django.db import models


class Celebrity(models.Model):
    name = models.CharField(max_length=200)
    
class Post(models.Model):
    celebrity = models.ForeignKey(Celebrity, on_delete=models.CASCADE)
    subject = models.CharField(max_length=30)
    content = models.TextField()
    create_date = models.DateTimeField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    
class NewCelebrity(models.Model):
    name = models.CharField(max_length=200)