from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    """
    Model to create notifications
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notifications'
    )
    # All possible notification types
    notification_type = (
        ("NEWPOST", "newpost"),
        ("FOLLOWED", "followed"),
        ("LIKEDPOST", "likedpost"),
        ("COMMENTED", "commented")
    )
    type = models.CharField(max_length=10, choices=notification_type, default="GENERAL")
    viewed = models.BooleanField(default=False)
    acting_user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_on']

    def __str__(self):
        return f"{self.type} followed by {self.acting_user}"