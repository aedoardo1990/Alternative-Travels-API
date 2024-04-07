from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model connected to 'owner' and 'followed'
    'owner' -> User that is following a User
    'followed' -> User that is followed by 'owner'
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following'
        )
    followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followed'
        )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f"{self.followed} followed by {self.owner}"
