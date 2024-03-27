from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def starting_page(request):
    return render(request, "blog/index.html")


def posts(request):
    pass


def post_detail(request, post):
    pass
