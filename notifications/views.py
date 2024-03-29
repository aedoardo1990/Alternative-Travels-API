from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Notification
from .serializers import NotificationSerializer


class NotificationList(generics.ListCreateAPIView):
    """
    view to check all notifications
    """ 
    permissions_classes=[permissions.IsAuthenticatedOrReadOnly]
    serializer_class=NotificationSerializer
    queryset=Notification.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NotificationDetail(generics.RetrieveDestroyAPIView):
    """
    view to retrieve a notification
    """
    permissions_classes = [IsOwnerOrReadOnly]
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()