from django import forms
from django.contrib.auth.forms import UserCreationForm

from news.models import Newspaper, Redactor


class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = ["title", "content", "published_date", "topic", "publishers"]
        widgets = {
            "published_date": forms.DateInput(attrs={"type": "date"}),
        }


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
        )
