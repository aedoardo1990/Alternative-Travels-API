from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):
    """
    Likes model connected to Owner and Post.
    'owner' is a User instance and 'post' is a Post instance.
    'unique_together' does not allow a user to like the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name ='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_at']
        unique_together=['owner', 'post']
    
    def __str__(self):
        return f"{self.post} from {self.owner}"