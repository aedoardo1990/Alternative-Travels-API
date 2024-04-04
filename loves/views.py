from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Love
from .serializers import LoveSerializer


class LoveList(generics.ListCreateAPIView):
    """
    view to create put to "love"/like a post
    """ 
    permissions_classes=[permissions.IsAuthenticatedOrReadOnly]
    serializer_class=LoveSerializer
    queryset=Love.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LoveDetail(generics.RetrieveDestroyAPIView):
    """
    view to retrieve or delete love/like on a post
    """
    permissions_classes = [IsOwnerOrReadOnly]
    serializer_class = LoveSerializer
    queryset = Love.objects.all()