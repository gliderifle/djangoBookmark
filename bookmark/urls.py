from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.bookmark_list),
    url(r'^\d/', views.bookmark_detail),
]