from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    view to follow a user
    """
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    view to retrieve followed user and to unfollow her/him
    """
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
    permissions_classes = [IsOwnerOrReadOnly]
