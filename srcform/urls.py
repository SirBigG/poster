from django.conf.urls import url
from .views import SearchFormView, HistoryView


urlpatterns = [
    url(r'^$', SearchFormView.as_view(), name='search_form'),
    url(r'^history/(?P<page>\d+)/$', HistoryView.as_view(), name='history_view'),
    ]
