# System libraries
# Third-party libraries
# Django modules
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.utils.http import is_safe_url
# Django apps
# Current-app modules
from .models import Tweet
from .forms import TweetForm

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request):
    context = {}
    return render(request, 'pages/feeds.html', context)


def create_tweet(request):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get('next')
    if form.is_valid():
        tweet = form.save(commit=False)
        tweet.save()
        if request.is_ajax():
            return JsonResponse(tweet.serialize(), status=201)
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    context = {
        'form': form
    }
    return render(request, 'includes/_modal.html', context)


def feeds(request):
    """
        Simple tweet feeds (list) API view
        Returns json data for consumption by all platforms
    """
    tweets = Tweet.objects.all()
    tweet_list = [t.serialize() for t in tweets]
    data = {
        'response': tweet_list
    }
    return JsonResponse(data)


def feed(request, tweet_id):
    """
        Simple tweet feed (Detail) API view
        Returns json data for consumption by all platforms
    """
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    data = {
        'id': tweet.id,
        'content': tweet.content
    }
    return JsonResponse(data)
