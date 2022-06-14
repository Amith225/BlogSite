from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=32)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
        labels = {'email': 'Email'}

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
