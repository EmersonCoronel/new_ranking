from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    full_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("full_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['full_name'].split()[0]
        user.last_name = ' '.join(self.cleaned_data['full_name'].split()[1:])
        if commit:
            user.save()
        return user
