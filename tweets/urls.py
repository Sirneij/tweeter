# Django modules
from django.urls import path
# Current-app modules
from .views import home_view, tweet_list, tweet_detail

app_name = 'tweets'
urlpatterns = [
    path("", home_view, name="home"),
    path("tweets/", tweet_list, name="tweet_list"),
    path("tweets/<int:tweet_id>", tweet_detail, name="tweet_detail"),
]
