from rest_framework import serializers
from .models import Post, Comment


class CommentModelSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['created_at']


class PostModelSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )
    comments = CommentModelSerializer(many=True, read_only=True, source = 'comment_set')
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['updated_at', 'created_at']
