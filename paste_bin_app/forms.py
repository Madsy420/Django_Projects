from django import forms
from paste_bin_app.models import PasteBinDB

class PasteBinDBForm(forms.ModelForm):
    url = forms.CharField(max_length = 264,required = False,widget = forms.HiddenInput)
    text = forms.CharField(widget = forms.Textarea)
    class Meta:        
        model = PasteBinDB
        fields = ('__all__')
        exclude = ['url']
