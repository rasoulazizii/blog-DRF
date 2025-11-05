from rest_framework import serializers
from .models import Post, Comment

class PostModelSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['updated_at', 'created_at']
