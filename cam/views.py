from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from cam.forms import Location_form


def home(request):
    return render(request,'users/home.html')

def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            return redirect('login')

    else:
        form = UserCreationForm()
    return render(request,'users/register.html', {'form' : form})


def location_logic(request):
    if request.method == 'POST':
        form= Location_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Location created successfully')

    else:
        form = Location_form()
    return render(request,'users/location_form.html', {'form' : form})



@login_required
def after_login(request):
    return render(request,'users/after_login.html')