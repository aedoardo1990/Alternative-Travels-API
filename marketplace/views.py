from django.db.models import Count
from rest_framework import permissions, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Marketplace
from .serializers import MarketplaceSerializer, MarketplaceDetailSerializer


class MarketplaceList(generics.ListCreateAPIView):
    """
    View to list posts on Marketplace
    """
    serializer_class = MarketplaceSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Marketplace.objects.annotate(
        comments_count = Count('comment', distinct=True),
        likes_count = Count('likes', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    ordering_fields = [
        'comments_count',
        'likes_count',
        'likes__created_at'
    ]
    search_fields = [
        'owner__username',
        'title',
        'condition',
        'price',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MarketplaceDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to check details of a post on Marketplace
    """
    serializer_class = MarketplaceDetailSerializer
    permission_classes = [ IsOwnerOrReadOnly]
    queryset = Marketplace.objects.annotate(
        comments_count = Count('comment', distinct=True),
        likes_count = Count('likes', distinct=True),
    ).order_by('-created_at')