from django import forms
from .models import Tweet


class TweetForm(forms.ModelForm):
    content = forms.CharField(max_length=240, required=True, widget=forms.TextInput(
        attrs={"placeholder": "Create a tweet", "class": "ribbitText"}))

    class Meta:
        model = Tweet
        fields = ("content",)

    def clean_content(self):
        content = self.cleaned_data.get("content")

        if len(content) > 240:
            raise forms.ValidationError("This tweet is too long")
        return content
