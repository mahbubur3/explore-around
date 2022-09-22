from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile


class SignupForm(UserCreationForm):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    email = forms.EmailField(label="Email Address", required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    
class EditUserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    
class ProfilePictureForm(forms.ModelForm):
     class Meta:
        model = UserProfile
        fields = ['profile_picture', ]