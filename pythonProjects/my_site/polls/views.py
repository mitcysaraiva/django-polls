from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse ('hello, world. youre at the polls index')
