from django import forms


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, label='Movie title',
                            widget=forms.TextInput(attrs={
                                'class': "form-control input-lg",
                                'placeholder': 'Enter the name of the movie',
                                'size': 40})
                            )

    def get_url(self):
        title = self.cleaned_data.get('title')
        title = title.split(' ')
        url = '+'.join(title)
        return url
