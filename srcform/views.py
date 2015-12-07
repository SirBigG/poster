from django.views.generic import FormView, ListView

from .forms import SearchForm
from .models import Poster, History

import urllib2
import json
import os


OMDBAPI_BASE_URL = 'http://www.omdbapi.com/?t='


class SearchFormView(FormView):
    template_name = 'search_form.html'
    form_class = SearchForm
    success_url = '/'

    def form_valid(self, form, **kwargs):
        """
        Check form.
        Return form and status message.
        """
        response = self.get_response(form)
        if response['Response'] == 'True':
            if response['Poster'] == 'N/A':
                message = "This movie doesn't have a poster."
                status = -2
            else:
                title = response['Title']
                poster = self.get_poster(response['Poster'])
                if not self.poster_in(title):
                    Poster.objects.create(title=title, poster=poster)
                    message = "Poster is found and save!!! You can find it in the 'History'."
                    status = 1
                else:
                    message = "Poster is in base already. You can look through your 'History'."
                    status = 2
                if self.need_change(title, poster):
                    pos = Poster.objects.get(title=title)
                    os.remove(pos.poster.url)
                    pos.update(poster=poster)
        else:
            message = "There is a mistake in your request :( Please try again!"
            status = -1
        History.objects.create(text=form.cleaned_data.get('title'), status=status)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['message'] = message
        return self.render_to_response(context)

    def get_response(self, form):
        """
        Passes to the OMDBAPI with user request and waits for a response.
        Return response in json.
        """
        url = OMDBAPI_BASE_URL + form.get_url()
        response = urllib2.urlopen(url)
        data = json.load(response)
        return data

    def get_poster(self, url):
        """
        Downloading poster and save it in /uploads/posters/ directory.
        Return path to this file.
        """
        poster = urllib2.urlopen(url).read()
        img_name = 'uploads/posters/%s' % url.split('/')[-1]
        f = open(img_name, 'wb')
        f.write(poster)
        f.close()
        return img_name

    def poster_in(self, title):
        """
        Return true if movie with this title in database else return false.
        """
        try:
            Poster.objects.get(title=title)
        except Poster.DoesNotExist:
            return False
        return True

    def need_change(self, title, poster):
        """
        Return true if poster name change else return false.
        """
        pos = Poster.objects.get(title=title)
        if pos.poster.name == poster:
            return False
        else:
            return True


class HistoryView(ListView):
    """
    Return history of search in reverse order.
    """
    model = Poster
    template_name = 'history.html'
    paginate_by = 20

    def get_queryset(self):
        return Poster.objects.order_by("-date")


class SearchHistoryView(ListView):
    """
    Return search history.
    """
    model = History
    template_name = 'search_history.html'
    paginate_by = 50

