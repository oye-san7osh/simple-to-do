from django import forms
from notes.models import Note


class CreateNote(forms.ModelForm):
    
    class Meta:
        model = Note
        fields = ["note_name", "note_detail"]