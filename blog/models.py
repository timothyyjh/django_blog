from typing import ContextManager
from django.db import models

# for default in date_posted
from django.utils import timezone

# for author
# one user can use multiple posts and 
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

