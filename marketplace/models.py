from django.db import models
from django.contrib.auth.models import User


class Marketplace(models.Model):
    """
    Model to post products to post items to sell on the Marketplace
    """
    image_filter_choices = [
    ('_1977', '1977'), ('brannan', 'Brannan'),
    ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
    ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
    ('kelvin', 'Kelvin'), ('normal', 'Normal'),
    ('nashville', 'Nashville'), ('rise', 'Rise'),
    ('toaster', 'Toaster'), ('valencia', 'Valencia'),
    ('walden', 'Walden'), ('xpro2', 'X-pro II')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=20)
    status = models.TextField(max_length=20)
    condition = models.TextField(max_length=20)
    details = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_post_g5kn5h',
        blank=True
    )
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=12)
    email = models.EmailField()
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'