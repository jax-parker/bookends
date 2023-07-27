from django.views.generic import ListView


class Index(ListView):
    template_name = 'home/index.html'
