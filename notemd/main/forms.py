from mdeditor.fields import MDTextFormField
from mdeditor.widgets import MDEditorWidget
from django import forms
from main.models import Note

class MDEditorForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'content': MDEditorWidget(config_name='default'),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    # 'style': 'max-width: 300px;',
                    'placeholder': 'Название',
                }
            )
        }
