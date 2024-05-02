from django import forms
from .models import Pattern_question,Normal_question

class Admin_Form(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)


class Normal_question_form(forms.ModelForm):
    class Meta:
        model=Normal_question
        fields=['question_name','question','a','b','c','d','answer','age']


class Pattern_question_form(forms.ModelForm):
    class Meta:
        model=Pattern_question
        fields=['question_name','question','question_image','a','b','c','d','answer','age']

