from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate
from.models import User


# Create your views here.


def home(request):
    user=User.objects.all
    context={'object':user}
    return render(request, 'dashboard/home.html', context)

def register(request):
    if request.method == 'POST':
        # Handle registration logic here
        pass
    return render(request, 'dashboard/index.html')


def login(request):
    pass



def logout(request):
    pass

def profile(request):
    pass

