from django.urls import path
from .views import AddBook, Books, BookDetail


urlpatterns = [
    path("", AddBook.as_view(), name="add_book"),
    path("books/", Books.as_view(), name="books"),
    path("<slug:pk>/", BookDetail.as_view(), name="book_detail"),
]
