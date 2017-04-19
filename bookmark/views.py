from django.shortcuts import render
from django.views.generic import ListView
from .models import Bookmark
from django.http import HttpResponse

# Create your views here.
def bookmark_list(request):
    return HttpResponse('bookmark_list')

def bookmark_detail(request):
    return HttpResponse('bookmark_detail')    

class BookmarkLV(ListView):
    model = Bookmark

bookmark_list = BookmarkLV.as_view()