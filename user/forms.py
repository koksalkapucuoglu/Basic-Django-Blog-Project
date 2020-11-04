from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label="Username")
    password = forms.CharField(max_length=20,label="Password",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label="Confirm Password",widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username") #submit edilmeden buradan girişleri alıyoruz.
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Password doesn't matct!")

        values = {
            "username" : username,
            "password" : password,
        } #sözlük biçiminde gönderiyoruz

        return values

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password",widget=forms.PasswordInput)

    