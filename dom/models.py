from django.db import models

# Create your models here.

class infa(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description')
    date = models.DateTimeField('Date and Time', auto_now_add=True)

    def __str__(self):
        return self.name
