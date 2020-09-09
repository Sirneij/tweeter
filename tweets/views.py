# System libraries
# Third-party libraries
# Django modules
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.utils.http import is_safe_url
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Django apps
# Current-app modules
from .models import Tweet
from .forms import TweetForm
from .serializers import TweetSerializer

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request):
    context = {}
    return render(request, 'pages/feeds.html', context)


@api_view(['POST'])
def create_tweet(request):
    serializer = TweetSerializer(data=request.POST or None)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)


@api_view(['GET'])
def feeds(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return Response(serializer.data, status=201)


@api_view(['GET'])
def feed(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    serializer = TweetSerializer(tweet)
    return Response(serializer.data, status=201)

# @login_required


def create_tweet_pure_django(request):
    user = request.user
    if not request.user.is_authenticated():
        user = None
        if request.is_ajax():
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)
    form = TweetForm(request.POST or None)
    next_url = request.POST.get('next')
    if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user = user or None
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


def feeds_pure_django(request):
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


def feed_pure_django(request, tweet_id):
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
