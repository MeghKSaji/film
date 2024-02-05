#Form definition

from django import forms
from cine.models import Cine
class Cineform(forms.ModelForm):

    class Meta:

        model=Cine
        fields="__all__"

