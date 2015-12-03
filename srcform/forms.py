from django import forms


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, label='Movie title')

    def get_url(self):
        title = self.cleaned_data.get('title')
        title = title.split(' ')
        url = '+'.join(title)
        return url
