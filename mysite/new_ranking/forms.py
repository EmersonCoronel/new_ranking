from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
