from django.conf.urls import include, url
from django.contrib import admin
from bookmark import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'gliderifle.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^bookmark/$', views.bookmark_list),
    url(r'^bookmark/$', views.BookmarkLV.as_view(), name="bookmark_list"),
    url(r'^bookmark/(?P<pk>\d+)$', views.bookmark_detail, name="bookmark_detail"),
    # url(r'^bookmark/', include('bookmark.urls')),
]
