# Django modules
from django.urls import path
# Current-app modules
from .views import home_view, tweets, tweet, create_tweet, delete_tweet, tweet_action

app_name = 'tweets'
urlpatterns = [
    path("", home_view, name="home"),
    path("newtweets/", create_tweet, name="new_tweet"),
    path("tweets/", tweets, name="tweets"),
    path("tweet/action/", tweet_action, name="tweet_action"),
    path("tweets/<int:tweet_id>/", tweet, name="tweet"),
    path("tweets/<int:tweet_id>/delete/", delete_tweet, name="delete_tweet"),
]
