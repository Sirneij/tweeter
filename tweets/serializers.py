from django.conf import settings
from rest_framework import serializers
from .models import Tweet


class TweetActionSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    action = serializers.CharField(required=True)

    def validate_action(self, value):
        value = value.lower().strip()
        if not value in settings.TWEET_VALID_OPTIONS:
            raise serializers.ValidationError('Tweet action not valid')
        return value


class TweetSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Tweet
        fields = ('id', 'content', 'likes',)

    def get_likes(self, obj):
        return obj.likes.count()

    def validate_content(self, value):
        if len(value) > settings.MAX_TWEET_LENGTH:
            raise serializers.ValidationError("This tweet is too long")
        return value
