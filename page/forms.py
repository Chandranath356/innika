from django import forms
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from .models import Page

class PageForm(forms.ModelForm):
     content = forms.CharField(widget = CKEditorWidget())
     class Meta:
        # specify model to be used
        model = Page
        fields = '__all__'
        labels ={
            'title':'Page Name',
            'slug':'Page Slug',
            'content':'Page Content'
        }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
            
            
        }