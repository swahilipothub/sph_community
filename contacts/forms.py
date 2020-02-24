from django import forms
from .models import Contact, Group

class GroupForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Group
        fields = ('name', )

class ContactForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    mobile = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    category = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset = None)

    class Meta:
        model = Contact
        fields = ('full_name', 'mobile', 'category')

    def __init__(self, user, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Group.objects.filter(user=user)

class UploadFileForm(forms.Form):
    file = forms.FileField()

