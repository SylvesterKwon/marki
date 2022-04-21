from django import forms
import django
from django.conf import UserSettingsHolder
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="E-mail")
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")