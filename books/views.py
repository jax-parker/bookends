from djando.views.generic import CreateView
from .models import Books
from .forms import BookForm

class AddBook(CreateView):
    """ Add book view """
    template_name = 'books/add_book.html'
    model = Books
    form_class = BookForm
    success_url = '/books/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddBook, self).form_valid(form)