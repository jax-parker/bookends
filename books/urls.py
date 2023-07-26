from django.urls import path
from .views import AddBook, Books


urlpatterns = [
    path('', AddBook.as_view(), name='add_book'),
    path('books/', Books.as_view(), name='books'),
]