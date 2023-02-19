from django import forms

from .models import Info

class InfoForm(forms.ModelForm): # insert new data
    name=forms.CharField(
      	widget=forms.TextInput(attrs={'placeholder':"Enter Your Name",
      		'class':'form-control'}))
    uid=forms.IntegerField(
      	widget=forms.NumberInput(attrs={'placeholder':"Enter Your Uid",
      		'class':'form-control'}))
    email=forms.EmailField(
      	widget=forms.EmailInput(attrs={'placeholder':"Enter Your Email",
      		'class':'form-control'}))
   
    gen=[("M",'Male'),
          ('F','Female'),
          ("O",'Other')]
    gender=forms.ChoiceField( choices=gen,
      	widget=forms.RadioSelect())


    location=forms.CharField(
      	widget=forms.TextInput(attrs={'placeholder':"Enter Your location",
      		'class':'form-control'}))

    cou=[("I",'India'),
         ("O",'Other')]
    country=forms.ChoiceField( choices=cou,
    	widget=forms.Select(attrs={'class':'form-control'}))
    
    class Meta:
    	model=Info
    	fields="__all__"

class UpdateForm(forms.Form):
  uid=forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder':"Enter Your Uid",
          'class':'form-control'}))
  name=forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':"Enter Your New Name",
          'class':'form-control'}))

class DelForm(forms.Form):    # accessing existing data
  uid=forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder':"Enter Uid to Delete Record",
          'class':'form-control'}))  



