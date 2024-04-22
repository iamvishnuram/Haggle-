from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Person
import os
import random
from PIL import Image, ImageDraw, ImageFont
from django.db import transaction

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=16, widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'profile_picture']

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')

        if not first_name or not last_name:
            raise forms.ValidationError('Both first name and last name are required.')
        
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.profile_picture = self.cleaned_data['profile_picture']

        # Generate a username with a mixture of first name, last name, and random 3-digit numbers
        username = f"{self.cleaned_data['first_name'].lower()}{self.cleaned_data['last_name'].lower()}{random.randint(100, 999)}"
        user.username = username

        initials = user.first_name[0].upper() + user.last_name[0].upper()
        filename = f'{initials}.png'
        filepath = os.path.join('static/profile_pics', filename)  # Save in static directory
        
        image = Image.new('RGB', (100, 100), color='white')
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        text_width, text_height = font.getsize(initials)
        draw.text(((100 - text_width) / 2, (100 - text_height) / 2), initials, fill='black', font=font)
        image.save(filepath)

        user.profile_picture = filepath  # Save the path to the image file

        if commit:
            user.save()
            Person.objects.create(
                user=user,
                name=f"{self.cleaned_data['first_name']} {self.cleaned_data['last_name']}",
                email=self.cleaned_data['email'],
                profile_picture=self.cleaned_data['profile_picture']
            )
        return user

