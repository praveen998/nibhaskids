from django import forms
from .models import Pattern_question,Normal_question
from .models import Enrolls,Classes,Subjects

class Admin_Form(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)


class Normal_question_form(forms.ModelForm):
    class Meta:
        model=Normal_question
        fields=['question_name','enroll_type','question','a','b','c','d','answer']


class Pattern_question_form(forms.ModelForm):
    class Meta:
        model=Pattern_question
        fields=['question_name','enroll_type','question','question_image','a','b','c','d','answer']


class Enrolls_form(forms.ModelForm):
    class Meta:
        model=Enrolls
        fields=['enroll_types']


class Classes_form(forms.ModelForm):
    class Meta:
        model=Classes
        fields=['class_types','enroll_id']


class Subjects_form(forms.ModelForm):
    class meta:
        model=Subjects
        fields=['subject_types','class_id']

  