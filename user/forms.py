from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from user.models import NewUser


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Şifrəniz', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Təkrar şifrəniz', widget=forms.PasswordInput)

    class Meta:
        model = NewUser
        fields = ('email', 'name', 'surname', 'group', 'password1', 'password2')


class UserLoginForm(forms.ModelForm):
    email = forms.CharField(label='Emailinizi daxil edin', widget=forms.TextInput
    (attrs={'placeholder': 'Emailinizi daxil edin'}))
    password = forms.CharField(label="Şifrəniz",
                               widget=forms.PasswordInput(attrs={'placeholder': 'Şifrənizi daxil edin'}))

    class Meta:
        model = NewUser
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Email və ya şifrə səhvdir")


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label=("İstifadəçi adınız"))
    first_name = forms.CharField(label=("Adınız"))
    last_name = forms.CharField(label=("Soyadınız"))
    group = forms.CharField(label=("Qrupunuz"))

    class Meta:
        model = NewUser
        fields = ['username', 'first_name', 'last_name', 'group']
