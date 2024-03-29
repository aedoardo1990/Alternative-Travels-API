from django.db.models import Count
from rest_framework import permissions, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer, TagSerializer, PostDetailSerializer


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
        likes_count = Count('likes', distinct=True),
        tags_count=Count("tags", distinct=True),
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
        "tags__name",
    ]
    # to filter posts 1) user is following, 2) posts user liked, 3) posts owned by a user
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
    serializer_class = PostDetailSerializer
    permission_classes = [ IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count = Count('comment', distinct=True),
        likes_count = Count('likes', distinct=True),
        tags_count=Count("tags", distinct=True),
    ).order_by('-created_at')

class TagList(generics.ListAPIView):
    """Lists all tags"""

    queryset = Post.tags.tag_model.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveAPIView):
    """Retrieves a tag"""

    queryset = Post.tags.tag_model.objects.all()
    serializer_class = TagSerializer