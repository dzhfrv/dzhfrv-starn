from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Vote
from .serializers import VoteSerializer


class VoteManager(ViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request):
        """POST /votes/ {'post': <pk>}"""
        data = dict()
        data['post'] = request.data['post']
        data['user'] = request.user.pk

        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response("success", status=status.HTTP_201_CREATED)

        existed_vote = Vote.objects.filter(
            user=request.user,
            post=data['post'],
        )
        existed_vote.delete()
        return Response("post already voted", status=status.HTTP_200_OK)
