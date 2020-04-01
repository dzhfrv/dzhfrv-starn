from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    last_update = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        exclude = ('author',)


class VoteField(serializers.RelatedField):
    def to_representation(self, value):
        return value.user.id


class DetailPostSerializer(PostSerializer):
    votes = VoteField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            'author', 'title', 'text', 'date_created', 'date_modified',
            'is_published', 'votes'
        )


