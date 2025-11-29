from django import forms
from .models import Tarefa
from projects.models import Project

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['title', 'project'] 

    def __init__(self, user, *args, **kwargs):
        super(TarefaForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(user=user)