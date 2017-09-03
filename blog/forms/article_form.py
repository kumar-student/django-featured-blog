from django import forms
from blog.models.articles import Article
# from django.forms.extras.widgets import SelectDateWidget

class ArticleForm(forms.ModelForm):
    # publish = forms.DateField(widget=SelectDateWidget())
    class Meta:
        model = Article
        fields = [
            "title",
            "description",
            "file",
            "highlight",
            "publish_date"
        ]