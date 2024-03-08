from django.db.models import Count
from rest_framework import permissions, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    View to list posts
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.annotate(
        comments_count = Count('comment', distinct=True),
        likes_count = Count('likes', distinct=True)
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
    ]
    # to filter posts user is following, posts user liked, posts owned by a user
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to check Post Details
    """
    serializer_class = PostSerializer
    permission_classes = [ IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count = Count('comment', distinct=True),
        likes_count = Count('likes', distinct=True)
    ).order_by('-created_at')