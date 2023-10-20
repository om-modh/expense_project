from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserProfileUpdate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileUpdate(request.POST)    
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Profile has been Updated!')
            return redirect('login')
    else:
        form = UserProfileUpdate()
        
    context = {
        'form' : form,
        'username' : user
    }
    return render(request, 'users/profile.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)    
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Account has been created! You can now Log in!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
            
