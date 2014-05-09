from django.shortcuts import render, render_to_response
from django.template import RequestContext


def home(request):
    context = {}
    return render_to_response("home.html", context, RequestContext(request))