from django import forms

class RegisterForm(forms.Form):
    avatar = forms.ImageField(required=False)
    age = forms.IntegerField(min_value=0, required=False)
    email = forms.EmailField(required=True)
    username = forms.CharField(min_length=3, required=True)
    password = forms.CharField(min_length=3, required=True)
    password_confirm = forms.CharField(min_length=3, required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if (password and password_confirm) and (password.lower() != password_confirm.lower()):
            raise forms.ValidationError(message="Password do not match")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField (min_length=3, required=True)  
    password = forms.CharField(min_length=3, required=True)