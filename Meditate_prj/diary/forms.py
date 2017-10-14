from django import forms

CHOICES=[('option1', 'option2', 'option3')]

class LogForm(forms.Form):
    like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    name = forms.CharField()
    message = forms.CharField()