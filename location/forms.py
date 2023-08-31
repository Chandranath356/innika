from django import forms
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from .models import Location

class LocationForm(forms.ModelForm):
    # title = forms.CharField(label='Location Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    # description = forms.CharField(label='Location Description',required=False,widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        # specify model to be used
        model = Location
        fields = '__all__'
        labels ={
            'title':'Location Name',
            'description':'Location Description',
            'images':'Images'
        }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'})
        }