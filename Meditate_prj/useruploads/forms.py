from django import forms
from .models import UploadImage, UploadAudio

class ImageForm(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = ['myimage']


class AudioForm(forms.ModelForm):
    class Meta:
        model = UploadAudio
        fields = ['myaudio']