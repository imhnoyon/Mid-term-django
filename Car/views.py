from django.shortcuts import render
from .models import Car
from . import forms
from Brand import models
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView

# Create your views here.

def Home(request,brand_slug=None):
    cars=Car.objects.all()
    if brand_slug is not None:
        Brands=models.Brands.objects.get(slug=brand_slug)
        cars=Car.objects.filter(brand=Brands)
        
    brandlist=models.Brands.objects.all()
    return render(request,'home.html',{'form':cars,'data':brandlist})




class AddCar_model(CreateView):
    model=Car
    form_class =forms.CarForm
    template_name = 'add_model.html'
    success_url = reverse_lazy('Add_car')
    def form_valid(self, form):
        return super().form_valid(form)
    






class CarDetailView(DetailView):
    model=Car
    pk_url_kwarg='id'
    template_name='car_detail.html'
    context_object_name = 'car'

    def post(self,request,*args,**kwargs):
        comment_form=forms.CommentForm(data=self.request.POST)
        post=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
        return self.get(request,*args,**kwargs)
              
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        post=self.object
        comments=post.comments.all()
        comment_form=forms.CommentForm()
        context['comments']=comments
        context['comment_form']=comment_form
        return context

