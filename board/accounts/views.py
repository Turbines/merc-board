from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import UpdateView, DetailView

from accounts import forms, models


def register(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST['email'], password=request.POST['password1'])
            login(request, user)
            return HttpResponseRedirect(reverse("profile", args=(user.id,)))
    else:
        form = forms.UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })


class ProfileDetailView(DetailView):
    model = models.User
    template_name = "accounts/profile.html"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):



        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['endorsements'] = {}
        return context


class ProfileUpdateView(UpdateView):
    form_class = forms.UserProfileForm
    model = models.User
    template_name = "accounts/profile-edit.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('profile', args=(self.request.user.id,))