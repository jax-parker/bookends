from django.views.generic import (CreateView, ListView, DetailView, DeleteView, UpdateView)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.db.models import Q
from .models import Books
from .forms import BookForm


class BooksView(ListView):
    """
    View all books
    """
    template_name = "books/books.html"
    model = Books
    context_object_name = "books"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            books = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(author__icontains=query) |
                Q(description__icontains=query) |
                Q(book_type__icontains=query)
            )
        else:
            books = self.model.objects.all()
        return books


class BookDetail(DetailView):
    """
    View to see a book in detail
    """
    template_name = "books/book_detail.html"
    model = Books
    context_object_name = "book"


class AddBook(LoginRequiredMixin, CreateView):
    """Add book view"""

    template_name = "books/add_book.html"
    model = Books
    form_class = BookForm
    success_url = "/books/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddBook, self).form_valid(form)

class EditReview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Edit a review """
    template_name = "books/edit_review.html"
    model = Books
    form_class= BookForm
    success_url = '/books'

    def test_func(self):
        return self.request.user == self.get_object().user


class ConfirmDelete(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """ Delete a book"""
    model = Books
    success_url = '/books/'
    template_name = "books/book_confirm_delete.html"

    def test_func(self):
        book = self.get_object()
        return self.request.user == book.user

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return self.model.objects.get(pk=pk)

class DeleteBook(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Books
    success_url = '/books/'

    def test_func(self):
        return self.request.user == self.get_object().user



