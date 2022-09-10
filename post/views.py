from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from .permissions import IsAuthorPermission, CommentPermission


from .models import Tweet, Comment
from .serializers import TweetSerializer, CommentSerializer


class TweetViewSet(ModelViewSet):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthorPermission, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [CommentPermission, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)