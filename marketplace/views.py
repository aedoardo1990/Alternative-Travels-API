from django.db.models import Count
from rest_framework import permissions, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Marketplace
from .serializers import MarketplaceSerializer

class MarketplaceList(generics.ListCreateAPIView):
    """
    View to list posts on Marketplace
    """
    serializer_class = MarketplaceSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Marketplace.objects.annotate(
        opinions_count = Count('opinion', distinct=True),
        loves_count = Count('loves', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    ordering_fields = [
        'opinions_count',
        'loves_count',
        'loves__created_at'
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
    serializer_class = MarketplaceSerializer
    permission_classes = [ IsOwnerOrReadOnly]
    queryset = Marketplace.objects.annotate(
        opinions_count = Count('opinion', distinct=True),
        loves_count = Count('loves', distinct=True),
    ).order_by('-created_at')
