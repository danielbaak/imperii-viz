from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from person import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^person/$',views.PersonView.as_view()),
    url(r'^person/(?P<pk>[0-9]+)/$',views.PersonDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
