from django.forms import ModelForm
from django import forms
from .models import Participant


CHOICES = [('Male', 'Female')]


class ParticipantForm(ModelForm):
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(
        attrs={'class': 'Radio radio-inline'}), choices=(('Male', 'Male'), ('Female', 'Female')))
    surname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Participant
        fields = 'surname', 'gender'
