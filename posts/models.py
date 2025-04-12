from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=60)
    post_content = models.TextField()
    # published_date = models.DateTimeField(auto_now=True)
    published_date = models.DateField(auto_now=True) # updating data type

    def __str__(self):
        return self.post_title
    