# System libraries
# Third-party libraries
# Django modules
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
# Django apps
# Current-app modules
from .models import Tweet
from .forms import TweetForm


def home_view(request):
    context = {}
    return render(request, 'pages/feeds.html', context)


def tweet_list(request):
    """
        Simple List API view
        Returns json data for consumption by all platforms
    """
    tweets = Tweet.objects.all()
    tweet_list = [{'id': t.id, 'content': t.content} for t in tweets]
    data = {
        'response': tweet_list
    }
    return JsonResponse(data)


def tweet_detail(request, tweet_id):
    """
        Simple Detail API view
        Returns json data for consumption by all platforms
    """
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    data = {
        'id': tweet.id,
        'content': tweet.content
    }
    return JsonResponse(data)
