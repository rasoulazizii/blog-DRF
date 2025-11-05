from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import PostModelSerializer
from .models import Post, Comment

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    permission_classes = [AllowAny]

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer



