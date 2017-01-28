from django.conf.urls import include, url
from django.contrib import admin
from haystack.views import SearchView
from haystack.forms import HighlightedSearchForm
from buginfo   import api_views
from buginfo import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'ecs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', SearchView(form_class=HighlightedSearchForm), name='haystack_search'),
    url(r'^buginfo/create/$', api_views.BugInfoView.as_view()),
    url(r'^bug_detail/(?P<pk>\d+)/$', views.BugDetailView.as_view() ,name ='bug_detail')
]
