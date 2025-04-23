from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Post(models.Model):
    post_title = models.CharField(max_length=60)
    post_content = models.TextField()
    # published_date = models.DateTimeField(auto_now=True)
    published_date = models.DateField(auto_now=True) # updating data type
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.post_title
    

class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

