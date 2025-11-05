from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import PostModelSerializer, CommentModelSerializer
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


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostCommentListView(generics.ListAPIView):
    serializer_class = CommentModelSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        return Comment.objects.filter(post_id=post_id).order_by('created_at')
    