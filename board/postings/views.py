from django.views.generic import CreateView
from postings import models


class PostingCreateView(CreateView):
    model = models.Posting
    fields = ['title', 'description', 'start', 'remote', 'public', 'tags']
    template_name = 'posting/create.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.poster = user
        return super(PostingCreateView, self).form_valid(form)