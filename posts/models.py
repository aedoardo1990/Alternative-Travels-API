from django.db import models
from django.contrib.auth.models import User
from tagulous.models import TagField
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video


class Post(models.Model):
    """
    Model to upload posts with images, tags and geolocation
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
    content = models.TextField(blank=True)
    tags = TagField(force_lowercase=True, max_count=15)
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.ImageField(
        upload_to='images/', default='../default_post_g5kn5h', null=True
    )
    video = models.FileField(
        upload_to='videos/',
        null=True, storage=VideoMediaCloudinaryStorage(),
        validators=[validate_video])
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
    
    def clean(self):
            if self.image and self.video:
                raise ValidationError(
                    'Please select only image or video, not both.')

            elif not self.image and not self.video:
                raise ValidationError(
                    'Please select image or video.')