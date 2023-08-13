from django import forms

class usersForm(forms.Form):
    num1=forms.CharField(label="First Number",required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    num2=forms.CharField(label="Second Number",required=False, widget=forms.TextInput(attrs={'class':'form-control'}))