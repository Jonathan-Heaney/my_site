from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    response_data = "Index"
    return HttpResponse(response_data)


def all_posts(request):
    response_data = "All Posts"
    return HttpResponse(response_data)


def show_post(request, post):
    response_data = f"Post Number {post}"
    return HttpResponse(response_data)
