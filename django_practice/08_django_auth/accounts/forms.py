from django.contrib.auth.forms import UserCreationForm,UserChangeForm

# 대신 다음과 같은 함수를 제공한다.
#  get_user_model은 현재 프로젝트에 활성화 되어있는 user 객체를 반환해준다.
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 현재 우리가 사용하는 user class로 재정의
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields =('email', 'first_name', 'last_name')