from django import forms
from .models import portal1

class user_form(forms.ModelForm):
    class Meta:
        model=portal1
        fields=['billID','rollno','name','invoiceno','indentno','bill']

