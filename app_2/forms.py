from django import forms
from django.core.exceptions import ValidationError
import re
from django.utils import timezone
class Formulario(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput, min_length=8)
    timestamp = forms.DateTimeField(widget=forms.HiddenInput, required=False, initial=timezone.now())

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password and username.lower() == password.lower():
            raise ValidationError('Error, el usuario y contraseña no pueden ser iguales')
        if username and password and username.lower() in password.lower():
            raise ValidationError('Error, la contraseña no puede contener el nombre de usuario')
        if len(password) < 8:
            raise ValidationError('Error, la contraseña es menor de 8 caracteres')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError('Error, la contraseña debe contener un caracter especial')
        if not re.search(r'[0-9]', password):
            raise ValidationError('Error, la contraseña debe contener un numero')
        if not re.search(r'[A-Z]', password):
            raise ValidationError('Error, la contraseña debe contener una letra mayuscula')
        if not re.search(r'[a-z]', password):
            raise ValidationError('Error, la contraseña debe contener una letra minuscula')
    def clean_timestamp(self):
        timestamp = self.cleaned_data.get('timestamp')
        if timestamp:
            current_time = timezone.now()
            if (current_time - timestamp).seconds > 120:
                raise ValidationError('Error, el formulario no puede enviarse 120 segundos después de haber accedido')