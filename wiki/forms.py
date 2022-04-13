from django import forms
from wiki.models import Article, Comment
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

from .models import Article

# Article 최초 생성시 사용 form
class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article 
        fields = ['title', 'content']
        labels = {
            'title': '제목',
            'content': '본문',
        }

    def clean_title(self): # 중복 article 체크
        data = self.cleaned_data['title']
        try:
            article_with_same_title = Article.objects.get(title=data)
        except Article.DoesNotExist: # 중복 article이 존재하지 않음
            pass
        else: # 중복 article이 존재함
            raise forms.ValidationError(mark_safe("이미 동일한 title을 가진 article이 있습니다."))

        return data


# Article 수정시 사용 form
class ArticleEditForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['content']
        labels = {
            'content': '본문',
        }

# Comment 생성 및 수정시 사용 form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['content']
        labels = {
            'content': '댓글',
        }

        
# Article 삭제시 사용 form
class ArticleDeleteConfirmationForm(forms.Form):
    confirmation_string = forms.CharField()

    def __init__(self, *args, **kwargs):
        self.article_title = kwargs.pop('article_title')
        super(ArticleDeleteConfirmationForm, self).__init__(*args, **kwargs)

    def clean_confirmation_string(self):
        data = self.cleaned_data['confirmation_string']
        if self.article_title != data:
            raise forms.ValidationError("확인문자가 일치하지 않습니다.")

        return data  

