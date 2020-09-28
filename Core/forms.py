from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fullname', 'email', 'phone', 'reg_no']
        labels = {'fullname': 'Full Name', 'email':'Email', 'phone':'Contact No.', 'reg_no':'Car Registration No.'}
        widgets = {'fullname': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.NumberInput(attrs={'class':'form-control'}),
            'reg_no': forms.TextInput(attrs={'class':'form-control'}),
        }