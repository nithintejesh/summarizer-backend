from django import forms

class URLForm(forms.Form):
    url = forms.URLField(label='Enter URL of the article page', widget=forms.TextInput(attrs={'placeholder': 'Enter URL...'}))
