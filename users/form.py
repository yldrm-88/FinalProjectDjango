from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import basvur

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2"]
        def __init__(self,*args,**kwargs):
            super(UserForm,self).__init__(*args,**kwargs)
            for name, field in self.fields.items():
                field.widget.attrs.update
                ({'class':'form-control'})



class BasvurForm(forms.ModelForm):
    class Meta: #meta modüllü ile hangi alanların dahil edileceğini ,hariç tutulacağını vs.
        model=basvur
        fields=['name','surname','email','number','file']
