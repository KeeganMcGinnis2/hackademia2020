from django.shortcuts import render, redirect
import random
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import SBUser

def home(request):
    return render(request, 'messaging/home.html')

@login_required
def index(request):
    return render(request, 'messaging/index.html')

@login_required
def room(request, room_name):
    user = request.user.username
    planet = SBUser.objects.get(username=user).planet
    return render(request, 'messaging/room.html', {
        'room_name': room_name,
        'user_id': user,
        'planet': planet
    })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'messaging/signup.html', {'form': form})