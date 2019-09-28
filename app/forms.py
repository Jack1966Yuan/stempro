from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app.models import CustomUser, SubscribeEmail, RegisterActive, SubscribePresentation
from datetime import date

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'portfolio_site', 'profile_pic')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email')

class RegisterActiveForm(forms.ModelForm):
    class Meta:
        model = RegisterActive
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'active_name', 'who_register', 'type',)

        widgets = {
            'active_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'who_register': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),            
        }

    def __init__(self, *args, **kwargs):
        super(RegisterActiveForm, self).__init__(*args, **kwargs)

TYPE_CHOICES = [
    ('Volunteer STEM Events', 'Volunteer STEM Events'),
    ('Volunteer Student Tutors', 'Volunteer Student Tutors'),
    ('Donation', 'Donation'),
]

class RegisterVoluteerForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    active_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    who_register = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    type = forms.CharField(
        max_length=3,
        widget=forms.Select(choices=TYPE_CHOICES, attrs={'class': 'form-control'}),
    )
  


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscribeEmail
        fields = ('subscribe_email',)

        widgets = {
            'subscribe_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email here*'}),
        }

    def __init__(self, *args, **kwargs):
        super(SubscribeForm, self).__init__(*args, **kwargs)
        self.fields['subscribe_email'].label = "Subscribe to Our News Letter!"


class SubscribePresentationForm(forms.ModelForm):
    class Meta:
        model = SubscribePresentation
        fields = ('name', 'number', 'email', 'cellphone', 'grade', 'wechat', 'schoolName', )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name here*'}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'How many come with you'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email here*'}),
            'cellphone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your cellphone here*'}),
            'grade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your grade here*'}),
            'wechat': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your webchat ID here'}),
            'schoolName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your school name here*'}),
        }

    def __init__(self, *args, **kwargs):
        super(SubscribePresentationForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Full Name"      
        self.fields['cellphone'].label = "Cell Phone"
        self.fields['schoolName'].label = "School Name"        
# class Contactform(forms.Form):
#   name = forms.CharField()
#   email = forms.EmailField(label='E-Mail')
#   category = forms.ChoiceField(choice=[('question', 'Question'), ('other', 'Other')]
#   subject = forms.CharField(required=False)
#   body = forms.CharField(widget=forms.Textarea)
