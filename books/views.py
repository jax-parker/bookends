from django.views.generic import (CreateView, ListView, DetailView, DeleteView)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Books
from .forms import BookForm


class BooksView(ListView):
    """
    View all books
    """
    template_name = "books/books.html"
    model = Books
    context_object_name = "books"


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

class DeleteBook(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete a book"""
    model = Books
    success_url = '/books/'

    def test_func(self):
        return self.request.user == self.get_object().user
