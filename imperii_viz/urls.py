from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from person.views import PersonView,PersonDetail,regentenList
from regeste.views import RegestDetail
from frontend.views import index_view, contact_view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^person/$',PersonView.as_view()),
    url(r'^person/(?P<pk>[0-9]+)/$',PersonDetail.as_view()),
    url(r'^person/(?P<person_id>[0-9]+)/regesten/$',regentenList),
    url(r'^regest/(?P<pk>[0-9]+)/$', RegestDetail.as_view()),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^$', index_view),
    url(r'^contact$', contact_view)
]

urlpatterns = format_suffix_patterns(urlpatterns)

