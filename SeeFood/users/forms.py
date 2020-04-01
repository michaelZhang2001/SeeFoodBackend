from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(required=False)

	class Meta:
		model = User
		fields = ['username','email','password1','password2']	#this specifies the fields that we want to WORK WITH, not the fields to be displayed(work with does imply display, since you have to display them to modify them)
		


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField(required=False)

	class Meta:
		model = User
		fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields = ['image']