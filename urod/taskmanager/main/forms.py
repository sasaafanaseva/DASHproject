from .models import Tasks
from django.forms import ModelForm, TextInput, Textarea
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label=u'ник')
    pass1 = forms.CharField(label=u'пароль')
    next = forms.CharField(widget=forms.HiddenInput(), required=False)


class TasksForm(ModelForm): #класс для парня
    class Meta:
        model = Tasks
        fields = ["title", "boy_age", "score", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи имя'
            }),
            "boy_age": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи возраст'
            }),
            "score": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи баллы'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Его поступок:'
            }),
        }
