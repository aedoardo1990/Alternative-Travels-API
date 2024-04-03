from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Available"), (1, "Sold"))


class Marketplace(models.Model):
    """
    Model to post products to post items to sell on the Marketplace
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    status = models.IntegerField(choices=STATUS, default=0)
    condition = models.CharField(max_length=255)
    details = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_post_g5kn5h',
        blank=True
    )
    address = models.CharField(max_length=255)
    contact_number = models.IntegerField()
    email = models.EmailField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'