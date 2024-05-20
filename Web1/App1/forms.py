from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True, label="User Name:")
    password = forms.CharField(required=True, label="Password:", widget=forms.PasswordInput)

class BorrowedForm(forms.Form):
    username = forms.CharField(required=True, label="User Name:")