from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blogapp.models import Profile


class ProfilePageForm(forms.ModelForm):
    model=Profile
    fields=('bio','profile_picture','website_url','fb_url','insta_url','twitter_url')
    widgets = {
        'bio':forms.Textarea(attrs={'class': 'form-control'   }), 
        #'profile_picture':forms.Select(attrs={'class': 'form-control'  }),
        'website_url':forms.TextInput(attrs={'class': 'form-control'  }),
        'fb_url':forms.TextInput(attrs={'class': 'form-control'  }),
        'insta_url':forms.TextInput(attrs={'class': 'form-control'}),
        'twitter_url':forms.TextInput(attrs={'class':'form-control'})
    }


class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    

    class Meta:
        model= User
        fields= {'username','first_name','last_name','email','password1','password2'}

    def __init__(self,*args,**kwargs):
        super (SignUpForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']='from-control'
        self.fields['password1'].widget.attrs['class']='from-control'
        self.fields['password2'].widget.attrs['class']='from-control'


class EditProfileForm(UserChangeForm):
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    is_superuser=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_stuff=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model= User
        fields= {'username','first_name','last_name','email','last_login','is_superuser','is_staff','is_active','date_joined'}


class PasswordChangingForm(PasswordChangeForm):
    old_password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))
    new_password1=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))
    new_password2= forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))

    class Meta:
        model= User
        fields= {'old_password','new_password1','new_password2'}