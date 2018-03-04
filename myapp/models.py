from django.db import models

# Create your models here.
class Entry(models.Model):
    name        = models.CharField(max_length=100, null=True)
    date        = models.DateTimeField(null=True)
    description = models.TextField(null=True)
    created     = models.DateTimeField(auto_now_add=True, null=True) 

    def __str__(self):
        return '{} {}'.format(self.name, self.date)
