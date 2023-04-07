from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget = forms.TextInput(
            attrs = {
                'class': 'my-title',
                'placeholder': '제목을 입력하세요',
            }
        ),
    )

    content = forms.CharField(
        label = '내용',
        widget = forms.Textarea(
            attrs = {
                'class': 'my-content',
                'placeholder': '내용을 입력하세요',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={'required': '내용을 입력하세요!'},
    )

    CATEGORY_CHOICES = [
        ('CS','CS'),
        ('개발','개발'),
        ('신기술','신기술'),
    ]
    category = forms.ChoiceField(
        label = '카테고리',
        widget = forms.Select(
            attrs = {
                'class': 'my-category',
            }
        ),
        choices = CATEGORY_CHOICES,
    )
    
    class Meta:
        model = Post
        fields = ('title', 'content', 'category')


