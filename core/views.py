from django.shortcuts import render,redirect
from .forms import SignupForm
from django.contrib.auth import login

# Create your views here.
def frontpage(request):
    return render(request,'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request,user)

            return redirect('frontpage')
        
    else:
        form=SignupForm()

    return render(request,'core/signup.html',{'form':form})