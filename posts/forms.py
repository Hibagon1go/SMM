from django import forms

from .models import Post

        
Category_Choices = (
    ('law_politics', '法学・政治学'),
    ('medical', '医学・薬学'),
    ('engineering', '工学'),
    ('social', '人文社会'),
    ('science', '理学'),
    ('agriculture', '農学'),
    ('economics', '経済学'),
    ('liberal_arts', '教養'),
    ('education', '教育学'),
) #分野の選択肢 added


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "picture", "text", "tags", "is_public")

class CategoryChoiceForm(forms.Form):
    choice = forms.ChoiceField(choices=Category_Choices, required=True)

        

    