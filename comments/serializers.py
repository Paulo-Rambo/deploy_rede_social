from rest_framework import serializers
from .models import Comment
from django.shortcuts import get_object_or_404


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'comment', 'created_at', 'user', 'publication']
        read_only_fields = ['id', 'created_at', 'user', 'publication']
