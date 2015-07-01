from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from search.views import SearchView
from person.views import PersonView,PersonDetail,regentenList
from regeste.views import RegestDetail


urlpatterns = [
    url(r'^search/', SearchView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^person/$',PersonView.as_view()),
    url(r'^person/(?P<pk>[0-9]+)/$',PersonDetail.as_view()),
    url(r'^person/(?P<person_id>[0-9]+)/regesten/$',regentenList),
    url(r'^regest/(?P<pk>[0-9]+)/$',RegestDetail.as_view()),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
