from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm as AuthPasswordChangeForm
from django.contrib.auth import password_validation
from django.core.validators import validate_email

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(required=True)
    agree_to_terms = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ("full_name", "username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Email"  # Change field label

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['full_name'].split()[0]
        user.last_name = ' '.join(self.cleaned_data['full_name'].split()[1:])
        if commit:
            user.save()
        return user
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        validate_email(username)  # This will raise ValidationError if email is not valid
        # Check if this username (email) is already taken
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This email is already in use.')
        return username

class CustomPasswordChangeForm(AuthPasswordChangeForm):
    old_password = forms.CharField(label='Old password', strip=False, widget=forms.PasswordInput(attrs={'autofocus': True}))
    new_password1 = forms.CharField(label='New password', widget=forms.PasswordInput, help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label='Confirm new password', widget=forms.PasswordInput, help_text='Enter the same password as before, for verification.')