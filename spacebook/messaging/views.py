from django.shortcuts import render
import random

def index(request):
    return render(request, 'messaging/index.html')

def room(request, room_name):
    return render(request, 'messaging/room.html', {
        'room_name': room_name,
        'user_id': random.randint(1,100) 
    })