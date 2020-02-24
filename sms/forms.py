from django import forms

from contacts.models import Group
from .models import Sms


class SmsForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset = None)
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = Sms
        fields = ('category', 'message')

    def __init__(self, user, *args, **kwargs):
        super(SmsForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Group.objects.filter(user=user)
