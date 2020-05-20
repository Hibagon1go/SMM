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
        choice = forms.fields.ChoiceField(choices=(
            ('法学・政治学', 'law_politics'),
            ('医学・薬学', 'medical'),
            ('工学', 'engineering'),
            ('人文社会', 'social'),
            ('理学', 'science'),
            ('農学', 'agriculture'),
            ('経済学', 'economics'),
            ('教養', 'liberal_arts'),
            ('教育学', 'education' ),
            ('ノンジャンル', 'nongenre')
        ),
        required=True, widget=forms.widgets.Select)     
        fields = ("title", "picture", "text", "is_public",
                  "law_politics", "medical", "engineering", "society", "science", "agriculture", "economics", "education", "liberal_arts", "nongenre") 






    