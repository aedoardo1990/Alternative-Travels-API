from rest_framework import serializers
from .models import Love


class LoveSerializer(serializers.ModelSerializer):
    """
    Serializer for Love Model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Love
        fields = [
            'id', 'owner', 'marketplace', 'created_at',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
