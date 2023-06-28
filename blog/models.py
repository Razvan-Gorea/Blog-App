from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # if author is deleted, delete the post(s) associated with that author
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # what appears on the admin page
    def __str__(self):
        return self.title

