from django.urls import path
from .views import (
    AddBook, BooksView, BookDetail,
    ConfirmDelete, DeleteBook, EditReview)
from . import views


urlpatterns = [
    path("user-books/", views.books, name="user_books"),
    path("add/", AddBook.as_view(), name="add_book"),
    path("confirm/<int:pk>", DeleteBook.as_view(), name="confirm_delete"),
    path("delete/<int:pk>/", ConfirmDelete.as_view(), name="delete_book"),
    path("edit/<int:pk>/", EditReview.as_view(), name="edit_review"),
    path("<int:pk>/", BookDetail.as_view(), name="book_detail"),
    path("", BooksView.as_view(), name="books"),
]

