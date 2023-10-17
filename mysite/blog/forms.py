from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
   name = forms.CharField(max_length=25)
   email = forms.EmailField()
   to = forms.EmailField()
   comments = forms.CharField(required=False, 
                              widget=forms.Textarea)

class CommentForm(forms.ModelForm):
   name = forms.CharField(label='Имя пользователя',
                               help_text= "Имя пользователя должно состоять макс из 150 символов",
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'autocomplete': "off"
                                                             }))
   email = forms.CharField(label='Почта',
                               widget=forms.EmailInput(attrs={'class': 'form-control'}))

   body = forms.CharField(label='Текст',
                               widget=forms.Textarea(attrs={'class': 'form-control'}))

   
   class Meta:
      model = Comment
      fields = ['name', 'email', 'body']
