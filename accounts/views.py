from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import Login_Form
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def doctors_list(request):
    doctors = User.objects.all()
    return render(request, 'user/doctors_list.html', {'doctors': doctors})

def doctors_detail(request, slug):
    doctors_detail = Profile.objects.get(slug = slug)
    return render(request, 'user/doctors_detail.html', {'doctors_detail': doctors_detail})

def user_login(request):
    if request.method == 'POST':
        form = Login_Form()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:doctors_list')
    else:
            form = Login_Form()
    return render(request, 'user/login.html',
                  {'form':form})

@login_required()
def myprofile(request):
    return render(request, 'user/myprofile.html',
                  )