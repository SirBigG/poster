from django import forms


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, label='Movie title')
    error_messages = {
        'incorrect_title': "'You enter incorrect movie title. Please try again!'",
        'poster_not_exist': "The movie don't have poster.",
    }

    def get_url(self):
        title = self.cleaned_data.get('title')
        title = title.split(' ')
        url = '+'.join(title)
        return url
