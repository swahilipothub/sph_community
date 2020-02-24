from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Profile, Company

class UserForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',)

class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), 
        max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'password')

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', )

class ProfileForm(forms.ModelForm):
    email=forms.EmailField(widget=forms.EmailInput())
    confirm_email=forms.EmailField(widget=forms.EmailInput())
    bio = forms.Textarea()

    class Meta:
        model = Profile
        fields = [
            'avatar',
            'mobile_number',
            'birth_date',
            'bio',
            'location',
            'city',
            'county',
            'country',
            'facebook',
            'twitter',
            'linkedin',
            'youtube',
        ]

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        # email = cleaned_data.get("email")
        # confirm_email = cleaned_data.get("confirm_email")
        bio = cleaned_data.get("bio")

        # if email != confirm_email:
        #     raise forms.ValidationError(
        #         "Emails must match!"
        #     )

        if len(bio) < 10:
            raise forms.ValidationError(
                "Bio must be 10 characters or longer!"
            )
    
    def save(self, *args, **kwargs):
        u = self.instance
        u.save()
        profile = super(ProfileForm, self).save(*args, **kwargs)
        return profile
    
class CompanyForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    africastalking_api_key = forms.CharField(
        widget=forms.TextInput(attrs={ 'class': 'form-control' }), 
        max_length=256, 
        required=False)
    africastalking_username = forms.CharField(
        widget=forms.TextInput(attrs={ 'class': 'form-control' }), 
        max_length=128, 
        required=False)
    africastalking_sender_id = forms.CharField(
        widget=forms.TextInput(attrs={ 'class': 'form-control' }), 
        max_length=128, 
        required=False)
    
    class Meta:
        model = Company
        fields = ['name', 'africastalking_api_key', 
            'africastalking_username', 'africastalking_sender_id']
