from django import forms

class SpisokForm(forms.Form):
    spisok_name = forms.CharField(max_length=100)

class TaskForm(forms.Form):
    task_name = forms.CharField(max_length=300)
