from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Vote.objects.all(),
                fields=['post', 'user']
            )
        ]
