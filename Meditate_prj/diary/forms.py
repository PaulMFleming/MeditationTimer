from django import forms
from .models import DiaryEntry


class DiaryEntryForm(forms.ModelForm):
    
    class Meta:
        model = DiaryEntry
        fields = ('title', 'content', 'intention')
