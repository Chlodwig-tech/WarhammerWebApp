from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Login"}))
    email    = forms.EmailField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Email"}))
    password1 = forms.CharField(label='', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Hasło'}))
    password2 = forms.CharField(label='', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Powtórz hasło'}))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )
    
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": "Login"}))
    password = forms.CharField(label='', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Hasło'}))