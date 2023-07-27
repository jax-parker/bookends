from django.views.generic import ListView
from books.models import Books


class Index(ListView):
    template_name = 'home/index.html'
    model = Books
    context_object_name = 'books'

    def get_queryset(self):
        return self.model.objects.all()[:3]
