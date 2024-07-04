from django.shortcuts import render
from . import forms
from .models import Brands
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView

from .models import Brands
# Create your views here.

class Add_brand(CreateView):
    model = Brands
    form_class =forms.BrandForm
    template_name = 'add_brand.html'
    success_url = reverse_lazy('add_brand')

    def form_valid(self, form):
        return super().form_valid(form)
    
    


