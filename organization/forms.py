from django import forms
from django.contrib.auth.models import User  # Use User if not using a custom user model

class organizationRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email Address', required=True)
    name = forms.CharField(label="Name", required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')  # Adjust fields if using a custom organization model

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():  # Check for existing email (modify for custom organization model)
            raise forms.ValidationError('This email address is already registered.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match.')
        return password2
from django.contrib.auth import authenticate

class organizationLoginForm(forms.Form):
    email = forms.EmailField(label='Email Address', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if email and password:
            organzation = authenticate(email=email, password=password)
            if not organzation:
                raise forms.ValidationError('Invalid email or password')
        return cleaned_data
