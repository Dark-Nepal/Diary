from django import forms
from django_quill.forms import QuillFormField
from .models import Diary

class QuillForm(forms.Form):
    content = QuillFormField()


class Entryform(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('title', 'content',)


