from django.urls import path
from .views import AddBook, BooksView, BookDetail, ConfirmDelete, DeleteBook


urlpatterns = [
    path("", AddBook.as_view(), name="add_book"),
    path("books/", BooksView.as_view(), name="books"),
    path("<slug:pk>/", BookDetail.as_view(), name="book_detail"),
    path("confirm/<slug:pk>", DeleteBook.as_view(), name="confirm_delete"), 
    path("delete/<slug:pk>/", ConfirmDelete.as_view(), name="delete_book"),
]
