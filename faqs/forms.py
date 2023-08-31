from django import forms
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from .models import Faqs

class FaqsForm(forms.ModelForm):
     class Meta:
        # specify model to be used
        model = Faqs
        fields = '__all__'
        labels ={
            'title':'Accordion Title',
            'content':'Accordion Description',
        }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            
        }