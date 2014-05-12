from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from . import forms


def home(request):
    context = {}
    return render_to_response("home.html", context, RequestContext(request))


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