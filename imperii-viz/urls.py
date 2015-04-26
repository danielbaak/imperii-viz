from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
import person.views as person_views
import search.views as search_views


urlpatterns = [
    url(r'^search/', search_views.SearchView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^person/$', person_views.PersonView.as_view()),
    url(r'^person/(?P<pk>[0-9]+)/$', person_views.PersonDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
