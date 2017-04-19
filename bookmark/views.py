from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bookmark_list(request):
    return HttpResponse('bookmark_list')

def bookmark_detail(request):
    return HttpResponse('bookmark_detail')    