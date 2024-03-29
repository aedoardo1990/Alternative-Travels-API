from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    """
    Serializer for Notification Model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    acting_user = serializers.ReadOnlyField(source='acting_user.username')
    acting_user_avatar = serializers.ReadOnlyField(
        source="acting_user.profile.avatar.url"
    )

    class Meta:
        model = Notification
        fields = [
            'id', 'owner', 'acting_user', 'created_at'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })