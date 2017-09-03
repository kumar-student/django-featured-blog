from django import forms
from blog.models.comments import Comment
# from django.forms.extras.widgets import SelectDateWidget

class CommentForm(forms.ModelForm):
    # publish = forms.DateField(widget=SelectDateWidget())
    class Meta:
        model = Comment
        fields = [
            "comment"
        ]