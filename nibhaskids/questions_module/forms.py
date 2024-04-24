from django import forms
class Admin_Form(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)