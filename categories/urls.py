from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CategoryListView, CategoryDetailView


urlpatterns = [
    url(r'^$', CategoryListView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', CategoryDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
