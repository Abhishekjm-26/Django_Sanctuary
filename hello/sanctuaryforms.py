from django import forms
from django.forms import ModelForm
from hello.models import sanctuary 

class sanctuaryForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = sanctuary
        fields = '_all_'
