from django.db import models
from django.contrib.auth.models import User
from marketplace.models import Marketplace


class Opinion(models.Model):
    """
     Model for comments connected to User and post on the Marketplace
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
