from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer

class CurrentUserSerializer(UserDetailsSerializer):
    """
    to retrieve user information of already registered user when logging in
    """
    profile_id = serializers.ReadOnlyField(source = 'profile.id')
    profile_image = serializers.ReadOnlyField(source = 'profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields = {
            'profile_id', 'profile_image'
        }