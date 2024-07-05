from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.views import LoginView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.models import User
from Car.models import Car
from Buy_Car.models import Purchase
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def Register(request):
    if request.method == 'POST':
        register_form=forms.RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('signin')
    else:
        register_form=forms.RegisterForm()
    return render(request,'signin_form.html',{'form':register_form,'type':'Signin'})


class user_login(LoginView):
    template_name='signin_form.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs) 
        context["type"] = 'Login'
        return context
    
@login_required
def Profile(request):
    purchase=Purchase.objects.filter(user=request.user)
    return render(request,'profile.html',{'forms':purchase})


@method_decorator(login_required,name='dispatch')
class EditProfileView(LoginRequiredMixin,UpdateView):
    model =User  
    form_class = forms.ChangeUserForm
    template_name = 'edit_profile.html'
    pk_url_kwarg='id'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        return super().form_valid(form)




@login_required
def user_logout(request):
    logout(request)
    return redirect('login')



# class CarDetailView(DetailView):
#     model=Car
#     template_name='profile.html'
#     context_object_name = 'car'






