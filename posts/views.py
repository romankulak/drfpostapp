from posts.models import Post
from posts.serializers import PostSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from posts.permissions import IsOwnerOrReadOnly, IsAccountOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    @action(
        detail=True,
        methods=['POST'], 
        permission_classes=[permissions.IsAuthenticated])
    def like(self, request, *args, **kwargs):
        post = self.get_object()
        is_liked = Post.objects.like_toggle(request.user, post)
        return Response({'liked': is_liked})

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAccountOwnerOrReadOnly,)
