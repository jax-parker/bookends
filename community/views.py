from django.views.generic import (CreateView, ListView, DeleteView, UpdateView)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Forum
from .forms import ForumForm


class AddPost(LoginRequiredMixin, CreateView):
    """Add a forum post """

    template_name = "community/add_post.html"
    model = Forum
    form_class = ForumForm
    success_url = "/forum/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPost, self).form_valid(form)
    