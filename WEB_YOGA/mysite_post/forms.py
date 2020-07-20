from django import forms
from .models import Blog_post, Login, UserSigin


class Blog_post_form(forms.ModelForm):
    class Meta:
        model = Blog_post
        fields = ('title', 'author_name', 'body', 'File_f')


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'
        labels = {
            'username': 'Username',
            'password': 'Password'}


class UserSiginform(forms.ModelForm):
    class Meta:
        model = UserSigin
        fields = '__all__'
        labels = {
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2'
        }
