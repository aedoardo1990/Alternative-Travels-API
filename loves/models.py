from django.db import models
from django.contrib.auth.models import User
from marketplace.models import Marketplace


class Love(models.Model):
    """
    Love model connected to Owner and Post.
    'owner' is a User instance and 'post' is a Post instance.
    'unique_together' does not allow a user to put a "love" to
    the same post on the marketplace twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE, related_name ='loves')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_at']
        unique_together=['owner', 'marketplace']
    
    def __str__(self):
        return f"{self.marketplace} from {self.owner}"