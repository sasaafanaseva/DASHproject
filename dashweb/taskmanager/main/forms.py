from django.contrib.auth.forms import AuthenticationForm, UsernameField

from .models import Tasks, Reviews
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from django.utils.translation import gettext, gettext_lazy as _


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': "current-password", 'class': 'form-control'}))

    class Meta:
        model = Tasks
        fields = ('username', 'fname', 'email', 'pass1', 'pass2')

    def save(self):
        pass


class TasksForm(ModelForm): #класс для парня
    class Meta:
        model = Tasks
        fields = ["title", "boy_age", "size"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи имя'
            }),
            "boy_age": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи возраст'
            }),
            "size": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'выбор:'
            }),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ["text"]

