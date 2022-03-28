from django import forms
from .models import Leads


class LeadsForm(forms.ModelForm):

    class Meta:
        model = Leads
        fields = ('name', 'phone', 'email', 'designation')