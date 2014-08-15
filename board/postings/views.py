from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.views.generic import CreateView, DetailView, UpdateView
import django_filters

from postings import models, forms


class PostingCreateView(CreateView):
    model = models.Posting
    fields = ['title', 'description', 'start', 'remote', 'public', 'tags']
    template_name = 'posting/create.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.poster = user.clientprofile
        return super(PostingCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')


class PostingDetailView(DetailView):
    model = models.Posting
    template_name = "posting/detail.html"
    context_object_name = "posting"


class PostingUpdateView(UpdateView):
    model = models.Posting
    template_name = "posting/update.html"
    fields = ('title', 'description', 'start', 'remote', 'public', 'tags')

    def get_object(self, queryset=None):
        posting = super(PostingUpdateView, self).get_object(queryset)
        if not posting.poster.user == self.request.user:
            raise PermissionDenied
        return posting


class PostingFeedFilter(django_filters.FilterSet):
    class Meta:
        model = models.Posting
        fields = ('remote',)

@login_required
def posting_feed(request):
    context = {}

    # permissioning
    queryset = models.Posting.objects.all()

    # filtering
    feed_filter = PostingFeedFilter(request.GET, queryset=queryset)
    context['filter'] = feed_filter

    # pagination
    paginator = Paginator(feed_filter.qs, 20)
    page = request.GET.get('page')
    try:
        postings = paginator.page(page)
    except PageNotAnInteger:
        postings = paginator.page(1)
    except EmptyPage:
        postings = paginator.page(paginator.num_pages)

    context['postings'] = postings


    return render_to_response('posting/feed.html', context, RequestContext(request))