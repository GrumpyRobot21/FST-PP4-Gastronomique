from django import forms
from .models import Reservations
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ReservationForm(forms.ModelForm):
    """Reservation form Model"""
    error_messages = {
        'username': {
            'required': 'Please enter a username.',
            'unique': 'This username is already taken. Please choose another.',
        },
        'email': {
            'required': 'Please enter your email address.',
            'unique': 'This email is already registered. Please add another.',
        },
        'password1': {
            'required': 'Please enter a password.',
            'min_length': 'Password must be at least 8 characters long.',
        },
        'password2': {
            'required': 'Please confirm your password.',
        },
    }

    class Meta:
        model = Reservations
        fields = ["name", "phone", "email", "date", "time", "guests"]


class UserRegistrationForm(UserCreationForm):
    """Use regitration model"""
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    """User login model"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ContactForm(forms.Form):
    """User Contact form model"""
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise forms.ValidationError(
                "Phone number must contain only digits.")
        return phone
