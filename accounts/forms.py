# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'phone_number', 'address', 'city', 'country', 'postal_code']

class SignUpForm(UserCreationForm):
    is_seller = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_seller']


from .models import SellerProfile

class SellerRegistrationForm(forms.ModelForm):
    class Meta:
        model = SellerProfile
        fields = []
