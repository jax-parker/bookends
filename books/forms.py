from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Books

class BookForm(forms.ModelForm):
    """ Form to create a new book """
    class Meta:
        model = Books
        fields = [
            'title',
            #'author',
            'description',
            'comments',
            'image',
            'image_alt',
            'book_type',
        ]

        comments = forms.CharField(widget=RichTextWidget())

        widget= {
            'description': forms.Textarea(attrs={"rows": 7}),
        }

        labels = {
            'title': 'Book Title',
            #'author' : 'Book Author',
            'description': 'Story Description',
            'comments': 'Book Review',
            'image': 'Book Image',
            'image_alt': 'Describe Book Cover',
            'book_type': 'Book Genre',
        }

