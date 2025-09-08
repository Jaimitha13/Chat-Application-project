from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Room, Message, UserProfile
from django.http import JsonResponse
from django.contrib.auth import logout
from django.views.decorators.http import require_http_methods
import json


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('index') 
    else:
        form = UserCreationForm()  # initialize a fresh form on GET
    
    return render(request, 'chat/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  
            return redirect('index')  
        else:
            error = "Invalid username or password"
            return render(request, 'chat/login.html', {'error': error})
    return render(request, 'chat/login.html')


@login_required
def index(request):
    rooms = Room.objects.all()
    online_users = UserProfile.objects.filter(online=True)
    return render(request, 'chat/index.html', {
        'rooms': rooms,
        'username': request.user.username,
        'online_users': online_users
    })



@login_required
def room(request, room_name):
    try:
        room = Room.objects.get(name=room_name)
    except Room.DoesNotExist:
        return redirect("index")
    
    messages = Message.objects.filter(room=room).order_by("timestamp")
    return render(request, 'chat/room.html', {
        'room': room,
        'messages': messages,
        'username': request.user.username
    })
@login_required
def create_room(request):
    if request.method == "POST":
        room_name = request.POST.get("room_name", "").strip()
        if room_name:
            room, created = Room.objects.get_or_create(
                name=room_name,
                defaults={'created_by': request.user}
            )
            return redirect("room", room_name=room.name)
    return redirect("index")


def logout_view(request):
    logout(request)
    return redirect('login_view')   # Redirect to login page after logout

