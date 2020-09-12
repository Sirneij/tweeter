from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
from .models import Tweet
User = get_user_model()


class TweetCaseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="sirneij@gmail.com", password="makesecretpass")

    def test_create_user(self):
        self.assertEqual(self.user.email, "sirneij@gmail.com")

    def test_create_tweet(self):
        tweet = Tweet.objects.create(
            user=self.user, content="I love learning and building stuff")
        self.assertEqual(tweet.user, self.user)
        self.assertEqual(tweet.id, 1)
