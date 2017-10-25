from django import forms
from .models import UploadImage

class ImageForm(forms.ModelForm):
    """
    Creates form for image uploads
    """
    class Meta:
        model = UploadImage
        fields = ['myimage']
