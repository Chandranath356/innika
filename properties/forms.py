from django import forms
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from .models import Properties,PropertiesImage
class DateInput(forms.DateInput):
      input_type = 'date'
class PropertyForm(forms.ModelForm):
    class Meta:
      model = Properties
      fields = '__all__'
      labels ={
            'title':'Property Name',
            'slug':'Property Slug',
            'content':'Property Description',
            'highlight':'Property Highlights',
            'files':'Images'
        }
      widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
            'type':forms.Select(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'start_form':forms.TextInput(attrs={'class':'form-control'}),
            'property_id':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'property_size':forms.TextInput(attrs={'class':'form-control'}),
            'year_of_bulit':DateInput(attrs={'class':'form-control'}),
            'bedroom':forms.TextInput(attrs={'class':'form-control'}),
            'bathroom':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
        }

class PropertyImageForm(forms.ModelForm):
   image = forms.ImageField(
      label="Property Image",
      widget=forms.ClearableFileInput(attrs={'multiple': 'TRUE','accept': 'image/*'})
   )

   class Meta:
      model = PropertiesImage
      fields = '__all__'
      