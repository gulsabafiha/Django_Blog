from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.views.generic import DetailView,CreateView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm,EditProfileForm,PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView
from blogapp.models import Profile


class ShowProfilePageView(DetailView):
    model= Profile
    template_name= 'registration/user_profile.html'
    

    def get_context_data(self,*args, **kwargs):
        users=Profile.objects.all()
        context = super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
        page_user=get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user']= page_user
        return context
"""
def detail_view(request, pk):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    context["data"] = Profile.objects.get(id = pk)
          
    return render(request, "user_profile.html", context)
"""

class EditProfilePageView(generic.UpdateView):
    model= Profile 
    template_name='registration/edit_profile.html'
    fields=['bio','profile_picture','website_url','fb_url','twitter_url','insta_url']
    success_url=reverse_lazy('home')

class CreateProfilePageView(CreateView):
    model=Profile
    template_name='registration/create_profile.html'
    fields='__all__'
    success_url=reverse_lazy('home')


    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
        


class PasswordsChangeView(PasswordChangeView):
    #form_class=PasswordChangeForm
    form_class=PasswordChangingForm
    template_name='registration/change-password.html'
    success_url= reverse_lazy('password_success')
    #success_url= reverse_lazy('home')

def password_success(request):
    return render(request,'registration/password_success.html',{})


class UserRegisterView(generic.CreateView):
    form_class= SignUpForm
    template_name= 'registration/register.html'
    success_url= reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class= EditProfileForm
    template_name= 'registration/added_profile.html'
    success_url= reverse_lazy('home')

    def get_object(self):
        return self.request.user

