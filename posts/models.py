from django.db import models
from django.contrib.auth.models import User
from tagulous.models import TagField
from cloudinary_storage.storage import VideoMediaCloudinaryStorage, MediaCloudinaryStorage
from django.core.files.storage import FileSystemStorage


class CustomStorage(FileSystemStorage):
    def get_valid_name(self, name):
        if name:
            if name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                # Images will be stored in Cloudinary using the MediaCloudinaryStorage
                return 'images/' + name
            elif name.endswith(('.mp4', '.mov', '.avi')):
                # Videos will be stored in Cloudinary using the VideoMediaCloudinaryStorage
                return 'videos/' + name
        # If the file extension is unknown or the instance/filename is not available,
        # use the default location and apply the default valid name logic
        return super().get_valid_name(name)


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
    image = models.FileField(upload_to = 'files/', storage=CustomStorage())
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    def save(self, *args, **kwargs):
        if self.test_upload:
            if self.test_upload.name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                # Use MediaCloudinaryStorage for images
                self.test_upload.storage = MediaCloudinaryStorage()
            elif self.test_upload.name.endswith(('.mp4', '.mov', '.avi')):
                # Use VideoMediaCloudinaryStorage for videos
                self.test_upload.storage = VideoMediaCloudinaryStorage()

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
