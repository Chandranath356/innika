from django import forms
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
     class Meta:
        # specify model to be used
        model = Testimonial
        fields = '__all__'
        labels ={
            'name':'Name',
            'content':'Testimonial Description',
            'designation':'Designation'
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'designation':forms.TextInput(attrs={'class':'form-control'}),
           
        }