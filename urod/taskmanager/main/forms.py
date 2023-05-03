from .models import Tasks
from django.forms import ModelForm, TextInput, Textarea
from django import forms


class LoginForm(forms.Form):
    # fname = forms.CharField(max_length=30, required=True, help_text='Required.')
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    username = forms.CharField(label=u'ник')
    pass1 = forms.CharField(label=u'пароль')
    next = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Tasks
        fields = ('username', 'fname', 'email', 'pass1', 'pass2')

    def save(self):
        pass


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
