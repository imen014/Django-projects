from . import forms

class FormulaireLogin(forms.Form):
    username = forms.CharField(max_length=50, label='username')
    password = forms.CharField(max_length=50, label='password', widget=forms.PasswordInput)


