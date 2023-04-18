from .models import Tasks
from django.forms import ModelForm, TextInput, Textarea


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