
from django import forms

from django.contrib.auth import get_user_model

User = get_user_model();


class GuestForm(forms.Form):
    Guest_email = forms.EmailField(
        widget = forms.EmailInput(
            attrs = {
                "class":"form-control",
                "placeholder": "Your email"
            }
        )
    )    


class LoginForm(forms.Form):

    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Enter your username to login"
            }

        )

    )
    password = forms.CharField(
            widget = forms.PasswordInput(
                attrs = {
                    "class": "form-control",
                    "placeholder": "enter your password",
                }
            )
    )



class RegisterForm(forms.Form):

    name = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class":"form-control",
                "placeholder": "Your first name"
            }
        )
    )
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs = {
                "class":"form-control",
                "placeholder": "Your email"
            }
        )
    )
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class":"form-control",
                "placeholder":"enter your display name"
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                "class":"form-control",
                "placeholder": "enter your password"
            }
        )
    )
    confirm_password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                "class":"form-control",
                "placeholder": "confirm your password"
            }
        )
    )
    # verify if username already exists

    def clean_username(self):
        
        username = self.cleaned_data.get("username")

        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username: {},exits please try another".format(qs[0]))
        return username

    def clean_email(self):

        email = self.cleaned_data.get("email")

        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("The email {}, exists please try another".format(email))

        return email

    # Define a function to handle the logics of validation

    # def clean_password(self):
    #     data = self.cleaned_data
    #     password = self.cleaned_data.get("password")
    #     confirm_password = self.cleaned_data.get("confirm_password")

    #     if password != confirm_password:
    #         raise forms.ValidationError("Passwords must match.")

    #     return data
