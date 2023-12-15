from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ('nome', 'username', 'email', 'password1', 'password2')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'})
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_superuser = True
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
