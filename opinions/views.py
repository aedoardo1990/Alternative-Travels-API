from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Opinion
from .serializers import OpinionSerializer, OpinionDetailSerializer


class OpinionList(generics.ListCreateAPIView):
    """
    View to get and post comments related to posts on the Marketplace
    """
    serializer_class = OpinionSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Opinion.objects.all()
    filter_backends = [
        DjangoFilterBackend
    ]
    # to get all the comments associated with a given post
    filterset_fields = [
        'marketplace',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OpinionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail view to check each comment
    """
    permissions_classes = [IsOwnerOrReadOnly]
    serializer_class = OpinionDetailSerializer
    queryset = Opinion.objects.all()
