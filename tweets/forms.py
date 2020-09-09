from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Tweet, CustomUser

MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class TweetForm(forms.ModelForm):
    content = forms.CharField(max_length=250, required=True, widget=forms.TextInput(
        attrs={"placeholder": "What's happening?", "class": "dark-mode-2 light-text border"}))

    class Meta:
        model = Tweet
        fields = ("content",)

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("This tweet is too long")
        return content
