from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import CreateView

from . import models


def home(request):
    context = {}
    return render_to_response("home.html", context, RequestContext(request))


class PostingCreateView(CreateView):
    model = models.Posting
    fields = ['title', 'description', 'start', 'remote', 'public', 'tags']
    template_name = 'posting/create.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.poster = user
        return super(PostingCreateView, self).form_valid(form)