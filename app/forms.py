from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import User, Item, Buyer, Profile
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm


class SignUpForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(required=False)
    password2 = password1

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
       

class ProfileForm(forms.ModelForm):
    CHOICES = (
        ('female', '女性',),
        ('male', '男性',)
    )
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=False)
  
    class Meta:
        model = Profile
        fields = ('gender', 'age')

class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label



class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name','image','status','size','category', 'memo', 'bought_by')
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder':'タイトルを入力'}),
                    'category': forms.RadioSelect(),
                    'size': forms.TextInput(attrs={'rows':1}),
                    'status': forms.RadioSelect(),
                    'memo': forms.Textarea(attrs={'rows':4}),
                    'bought_by': forms.TextInput(attrs={'rows':1}),
                  }

class BuyerForm(forms.ModelForm):

    class Meta:
        model = Buyer
        fields = ('buyername', 'email','gender','age', 'adress')
        widgets = {
                    'buyername': forms.TextInput(attrs={'placeholder':'氏名を入力'}),
                    'email': forms.TextInput(attrs={'placeholder':'メールアドレスを入力'}),
                    'gender': forms.RadioSelect(),
                    'age': forms.TextInput(attrs={'rows':1}),
                    'adress': forms.TextInput(attrs={'placeholder':'住所を入力'}),
                  }