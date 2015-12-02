from django.views.generic import FormView, ListView
from django.forms.utils import ErrorList

from .forms import SearchForm
from .models import Poster

import urllib2
import json


OMDBAPI_BASE_URL = 'http://www.omdbapi.com/?t='


class SearchFormView(FormView):
    template_name = 'search_form.html'
    form_class = SearchForm
    success_url = '/history/1/'

    def form_valid(self, form):
        response = self.get_response(form)
        if response['Response'] == 'True':
            if response['Poster'] == 'N/A':
                # TODO: return message
                raise ErrorList('p')
            else:
                title = response['Title']
                poster = self.get_poster(response['Poster'])
                if not self.poster_in(title):
                    Poster.objects.create(title=title, poster=poster)
        else:
            # TODO: return message
            raise ErrorList('q')
        return super(SearchFormView, self).form_valid(form)

    def get_response(self, form):
        url = OMDBAPI_BASE_URL + form.get_url()
        response = urllib2.urlopen(url)
        data = json.load(response)
        return data

    def get_poster(self, url):
        poster = urllib2.urlopen(url).read()
        img_name = 'uploads/posters/%s' % url.split('/')[-1]
        f = open(img_name, 'wb')
        f.write(poster)
        f.close()
        return img_name

    def poster_in(self, title):
        try:
            Poster.objects.get(title=title)
        except Poster.DoesNotExist:
            return False
        return True

    # TODO: if poster changed



class HistoryView(ListView):
    model = Poster
    template_name = 'history.html'
    paginate_by = 20

    def get_queryset(self):
        return Poster.objects.order_by("-date")
