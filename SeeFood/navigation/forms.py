from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import string

class KeyWordSearchForm(forms.Form):
    keyword = forms.CharField(help_text = "enter a restaurant name or any keyword")

    def clean_keyword(self):
        data = self.cleaned_data['keyword']

        if(data == ""):
            raise ValidationError(_('Please enter a keyword'))
        if(string.punctuation in data):
            raise ValidationError(_('Please enter a valid keyword'))
        
        return data
