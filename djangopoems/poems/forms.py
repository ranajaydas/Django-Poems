from django import forms
from .models import Poem


class PoemForm(forms.ModelForm):
    class Meta:
        model = Poem
        fields = '__all__'

    def clean_slug(self):
        return self.cleaned_data['slug'].lower()
