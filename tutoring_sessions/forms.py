from .models import Session
from django import forms

class SessionRequestForm(forms.ModelForm):

    class Meta():
        model = Session
        fields = ('student_username', 'student_name', 'tutor_name', 'description', 'time')
