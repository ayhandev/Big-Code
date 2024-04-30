from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Create username')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Create password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class SignInForm(AuthenticationForm):
    username = forms.CharField(label='Your username')
    password1 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'password1')


class EditProfileForm(forms.ModelForm):
    model = Profile
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email address')
    fields = ['avatar', 'about']

    class Meta:
        model = User
        fields = ( 'username', 'email')


class ResetPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Old password',
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(),
        label='New password',
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Repeat new password'
    )

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'about']
