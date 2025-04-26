from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room,Message
# Create your views here.


@login_required
def rooms(req):
    rooms = Room.objects.all()
    return render(req,'rooms/rooms.html',{'rooms':rooms})

@login_required
def room_fetch(req,slug):
    rooms = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=rooms)[0:25]

    return render(req,'rooms/room.html',{'room':rooms,'messages':messages})

