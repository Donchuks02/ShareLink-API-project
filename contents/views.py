from django.contrib.auth import get_user_model
from rest_framework import generics
from .models import Content
from .permissions import IsOwnerOrReadOnly
from .serializers import ContentSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser

# Create your views here.

class ContentList(generics.ListCreateAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Content.objects.all()
  serializer_class = ContentSerializer

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class ContentDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Content.objects.all()
  serializer_class = ContentSerializer

class UserList(generics.ListCreateAPIView):
  permission_classes = [IsAdminUser]
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer
