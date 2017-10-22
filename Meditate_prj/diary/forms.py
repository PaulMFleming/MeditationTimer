from django import forms
from .models import DiaryEntry, BODY_CHOICES, MIND_CHOICES


class DiaryEntryForm(forms.ModelForm):
    body = forms.ChoiceField(widget=forms.RadioSelect(),choices=BODY_CHOICES, label="How did your body feel during your meditation? My body felt")
    mind = forms.ChoiceField(widget=forms.RadioSelect(),choices=MIND_CHOICES, label="How did your mind feel during your meditation? My mind")
    insights = forms.CharField(widget=forms.Textarea, label="Did you have any thoughts, feelings or insights you'd like to record?")

    class Meta:
        model = DiaryEntry        
        fields = ('body', 'mind', 'insights')

