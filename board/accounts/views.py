from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext

from . import forms


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


def profile(request):
    if request.method == 'POST':
        form = forms.UserProfileForm(request.POST)
        if form.is_valid():
            updated_user = form.save()
            return HttpResponseRedirect('profile')
    else:
        form = forms.UserCreationForm(request.user)

    return render(request, "profile.html", {'form': form})