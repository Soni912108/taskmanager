from django import forms
from django.contrib.auth.models import User
from .models import User, Task


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, label='Username')
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        help_text='Your password should include at least one capital letter, one number, and one special character.'
    )
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        """
        Check that the username is not already taken
        """
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')
        return username

    def clean_password1(self):
        """
        Check that the password meets the complexity requirements
        """
        password1 = self.cleaned_data.get('password1')
        if not any(char.isupper() for char in password1):
            raise forms.ValidationError('Password should contain at least one capital letter.')
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError('Password should contain at least one number.')
        if not any(char in '!@#$%^&*()' for char in password1):
            raise forms.ValidationError('Password should contain at least one special character.')
        return password1

    def clean_password2(self):
        """
        Check that the two password entries match
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')
        return password2
    







class TaskForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    completed = forms.BooleanField(required=False)

    class Meta:
        model = Task
        fields = ['title', 'description', 'image', 'completed']