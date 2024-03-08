from django.db.models import Count
from rest_framework import permissions, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListCreateAPIView):
    """
    to view list of profiles
    """
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count = Count('owner__post', distinct=True),
        followers_count = Count('owner__followed', distinct=True),
        following_count = Count('owner__following', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]
    filterset_fields = [
        # to get all profiles that are following a profile, given its id
        'owner__following__followed__profile',
        # to get all profiles that are followed by a profile, given its id
        'owner__followed__owner__profile'
    ]
    

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    to view the detail of a profile. it can be edited/deleted only by the owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count = Count('owner__post', distinct=True),
        followers_count = Count('owner__followed', distinct=True),
        following_count = Count('owner__following', distinct=True)
    ).order_by('-created_at')