from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import PrivateMessage
from django.db.models import Q

@login_required
def private_chat(request, username):
    other_user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            PrivateMessage.objects.create(
                sender=request.user,
                receiver=other_user,
                message=message
            )
            return redirect('private_chat', username=other_user.username)

    messages = PrivateMessage.objects.filter(
        sender__in=[request.user, other_user],
        receiver__in=[request.user, other_user]
    )
    return render(request, 'chat/private_chat.html', {
        'messages': messages,
        'other_user': other_user
    })

@login_required
def redirect_to_chat(request):
    username = request.GET.get('username')
    return redirect('private_chat', username=username)


@login_required
def chat_list(request):
    user = request.user

    # Get all users that this user has exchanged messages with
    message_users = PrivateMessage.objects.filter(
        Q(sender=user) | Q(receiver=user)
    ).values_list('sender', 'receiver')

    user_ids = set()
    for sender_id, receiver_id in message_users:
        if sender_id != user.id:
            user_ids.add(sender_id)
        if receiver_id != user.id:
            user_ids.add(receiver_id)

    users = User.objects.filter(id__in=user_ids)
    return render(request, 'chat/chat_list.html', {'users': users})

@login_required
def redirect_to_chat(request):
    # Redirects to the chat list page
    return redirect('chat_list')