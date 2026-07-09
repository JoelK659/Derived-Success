from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    education_level = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'education_level', 'phone_number', 'password1', 'password2')

    def __init__(self, *args, **keyargs):
        super(RegisterUserForm, self).__init__(*args, **keyargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=True)

        Profile.objects.create(
            user=user,
            education_level=self.cleaned_data['education_level'],
            phone_number=self.cleaned_data['phone_number']
        )

        return user
