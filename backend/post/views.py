from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


class PostManager(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        """GET /api/v1/posts/"""
        queryset = Post.objects.filter(author=request.user)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """POST /api/v1/posts/"""
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save(author=request.user)
        return Response({'id': post.id}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """GET /api/v1/posts/<pk>/"""
        queryset = Post.objects.filter(author=request.user)
        user = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(user)
        return Response(serializer.data)
