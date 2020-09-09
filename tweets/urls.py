# Django modules
from django.urls import path
# Current-app modules
from .views import home_view, feeds, feed, create_tweet

app_name = 'tweets'
urlpatterns = [
    path("", home_view, name="home"),
    path("newtweets/", create_tweet, name="new_tweet"),
    path("tweets/", feeds, name="feeds"),
    path("tweets/<int:tweet_id>", feed, name="feed"),
]
