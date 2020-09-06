# System libraries
# Third-party libraries
# Django modules
from django.db import models
# Django apps
# Current-app modules


class Tweet(models.Model):
    """Model definition for Tweet."""

    content = models.TextField()
    image = models.FileField(
        upload_to='images/', max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for Tweet."""
        ordering = ['-created', ]
        verbose_name = 'Tweet'
        verbose_name_plural = 'Tweets'

    def __str__(self):
        """Unicode representation of Tweet."""
        return f'{self.content}'
