# System libraries
# Third-party libraries
# Django modules
from django.conf import settings
from django.db import models
# Django apps
# Current-app modules

User = settings.AUTH_USER_MODEL


class Tweet(models.Model):
    """Model definition for Tweet."""
    user = models.ForeignKey(User, verbose_name=_(""),
                             on_delete=models.CASCADE)
    content = models.TextField()
    image = models.FileField(
        upload_to='images/', max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for Tweet."""
        ordering = ['-id', ]
        verbose_name = 'Tweet'
        verbose_name_plural = 'Tweets'

    def __str__(self):
        """Unicode representation of Tweet."""
        return f'{self.content}'

    def serialize(self):
        data = {
            "id": self.id,
            "content": self.content
        }
        return data
