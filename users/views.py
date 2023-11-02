from django.shortcuts import render, redirect
from .forms import UserRegistrationForm,  UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('manager-home')
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'username': user,
        'form': form,
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
            
