from rest_framework import serializers
from .models import Post
from likes.models import Like
from tagulous.contrib.drf import TagSerializer


class PostSerializer(TagSerializer, serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source = 'owner.profile.id')
    profile_image = serializers.ReadOnlyField(source = 'owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    tags_count = serializers.IntegerField(read_only=True)

    def validate_image(self, value):
        """checks if image bigger than 2MB, width & height larger than 4096 px"""
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value
    
    def validate_video(self, value):
        if value.size > 1024 * 1024 * 60:
            raise serializers.ValidationError(
                'Video size larger than 60 MB!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
                ).first()
            # print(like_post)
            return like.id if like else None
        return None
    
    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter',
            'like_id', 'comments_count', 'likes_count',
            'tags', 'tags_count', 'latitude', 'longitude',
            'video'
        ]


class PostDetailSerializer(PostSerializer):
    """Serializer for Post update view with geolocation. Makes required 
    fields optionalfor PUT requests."""

    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag model."""

    class Meta:
        model = Post.tags.tag_model
        fields = ["id", "name"]