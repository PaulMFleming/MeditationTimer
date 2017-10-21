from django import forms
from .models import DiaryEntry, FORM_CHOICES


class DiaryEntryForm(forms.ModelForm):
    body = forms.ChoiceField(widget=forms.RadioSelect(),choices=FORM_CHOICES)
    mind = forms.ChoiceField(widget=forms.RadioSelect(),choices=FORM_CHOICES)

    class Meta:
        model = DiaryEntry        
        fields = ('body', 'mind', 'insights')

