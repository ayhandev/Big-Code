from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class infa(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description')
    date = models.DateTimeField('Date and Time', auto_now_add=True)

    def __str__(self):
        return self.name


class PublishedCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField()
    description = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Code by {self.user.username} published on {self.date_published}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    published_code = models.ForeignKey(PublishedCode, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.published_code}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    published_code = models.ForeignKey(PublishedCode, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"Like by {self.user.username} on {self.published_code}"