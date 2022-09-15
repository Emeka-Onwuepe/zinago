from django import forms
from django.db import models
from .models import Application

class application_form(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ("selected","employed")
        