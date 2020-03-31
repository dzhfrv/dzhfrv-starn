from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    last_update = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        exclude = ('author',)

