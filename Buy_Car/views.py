from django.shortcuts import render,redirect
from .models import Purchase
from Car.models import Car
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def buy_car(request, id):
    car = Car.objects.get(pk=id)
    if car.quantity > 0:
        form= Purchase.objects.create(user=request.user, car=car)
        form.save()
        car.quantity -= 1
        car.save()    
        return redirect('profile')
    else:
        car = Car.objects.get(pk=id)
    return render(request,'car_detail.html')
    
