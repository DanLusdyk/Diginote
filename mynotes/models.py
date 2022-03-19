from datetime import datetime
from django.utils import timezone
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    lastUpdated = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        self.lastUpdated = timezone.now()
        return super(Note, self).save(*args, **kwargs)
