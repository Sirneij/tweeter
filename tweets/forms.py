from django import forms
from .models import Tweet

MAX_TWEET_LENGTH = 250


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
