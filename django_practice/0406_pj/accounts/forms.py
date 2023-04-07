from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    birthday = forms.DateField(
        label = '생년월일',
        widget=forms.widgets.DateInput(attrs={'type':'date'})
    )

    # username 필드의 도움말 텍스트를 비움
    username = forms.CharField(help_text='', label='아이디',)
    # password1 필드의 도움말 텍스트를 비움
    password1 = forms.CharField(help_text='', label='패스워드',)
    # password2 필드의 도움말 텍스트를 비움
    password2 = forms.CharField(help_text='', label='패스워드 확인',)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name','birthday', 'password1', 'password2',)

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)






