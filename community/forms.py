from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Forum


class ForumForm(forms.ModelForm):
    """Form to create a new forum post """

    class Meta:
        model = Forum
        fields = [
            "subject",
            "post",
        ]

        post = forms.CharField(widget=RichTextWidget())

        widget = {
            "subject": forms.Textarea(attrs={"rows": 7}),
        }

        labels = {
            "subject": "Subject",
            'post' : 'Comments',
        }

