from django import forms
from .models import ChitRegistration

class ChitForm(forms.ModelForm):

    registration_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=False)

    class Meta:
        model = ChitRegistration
        fields = ['chit_Type', 'chit_Number','name', 'phoneNumber', 'address', 'num_Of_Chits']
