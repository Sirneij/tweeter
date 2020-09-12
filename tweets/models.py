# System libraries
# Third-party libraries
# Django modules
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models
# Django apps
# Current-app modules


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Tweet(models.Model):
    """Model definition for Tweet."""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        CustomUser, blank=True, related_name='tweet_user', through='TweetLike')
    content = models.TextField(null=True, blank=True)
    image = models.FileField(
        upload_to='images/', max_length=100, null=True, blank=True)
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Tweet."""
        ordering = ['-id', ]
        verbose_name = 'Tweet'
        verbose_name_plural = 'Tweets'

    def __str__(self):
        """Unicode representation of Tweet."""
        return f'{self.content}'

    @property
    def is_retweeted(self):
        return self.parent != None

    def serialize(self):
        data = {
            "id": self.id,
            "content": self.content
        }
        return data


class TweetLike(models.Model):
    """Model definition for TweetLike."""

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for TweetLike."""

        verbose_name = 'TweetLike'
        verbose_name_plural = 'TweetLikes'

    def __str__(self):
        """Unicode representation of TweetLike."""
        return self.tweet.content
