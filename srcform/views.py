from django.views.generic import FormView, ListView

from .forms import SearchForm
from .models import Poster

import urllib2
import json
import os


OMDBAPI_BASE_URL = 'http://www.omdbapi.com/?t='


class SearchFormView(FormView):
    template_name = 'search_form.html'
    form_class = SearchForm
    success_url = '/'

    def form_valid(self, form, **kwargs):
        response = self.get_response(form)
        if response['Response'] == 'True':
            if response['Poster'] == 'N/A':
                message = "This movie doesn't have a poster."
            else:
                title = response['Title']
                poster = self.get_poster(response['Poster'])
                if not self.poster_in(title):
                    Poster.objects.create(title=title, poster=poster)
                    message = "Poster is found!!! You can find it in the 'History'."
                else:
                    message = "Poster is in base already. You can look through your 'History'."
                if self.need_change(title, poster):
                    pos = Poster.objects.get(title=title)
                    os.remove(pos.poster.url)
                    pos.update(poster=poster)
        else:
            message = "There is a mistake in your request :( Please try again!"

        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['message'] = message
        return self.render_to_response(context)

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

    def need_change(self, title, poster):
        pos = Poster.objects.get(title=title)
        if pos.poster.name == poster:
            return False
        else:
            return True


class HistoryView(ListView):
    model = Poster
    template_name = 'history.html'
    paginate_by = 20

    def get_queryset(self):
        return Poster.objects.order_by("-date")
