from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def bookmark_list(request):
    return render(request, 'bookmark/bookmark_list.html',{
        'bookmark_list': Bookmark.object.all(),
    })

def bookmark_detail(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    return render(request, 'bookmark/bookmark_detail.html',{
        'bookmark': bookmark,
    })

class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark

bookmark_list = BookmarkLV.as_view()
boormark_detail = BookmarkDV.as_view()