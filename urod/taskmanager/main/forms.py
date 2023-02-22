from .models import Tasks
from django.forms import ModelForm, TextInput, Textarea


class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введи имя'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Его поступок:'
            }),
        }