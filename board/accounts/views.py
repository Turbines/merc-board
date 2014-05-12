from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import UpdateView

from . import forms, models


def register(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = forms.UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })


class ProfileUpdateView(UpdateView):
    form_class = forms.UserProfileForm
    model = models.User
    template_name = "profile.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('profile')