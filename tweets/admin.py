# Django modules
from django.contrib import admin

# Current-app modules
from .models import Tweet
admin.site.register(Tweet)
