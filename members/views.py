from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
# from django.contrib.auth import authenticate, login, logout

# Create your views here.
class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class RegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class EditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
