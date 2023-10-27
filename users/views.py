from django.shortcuts import render, redirect
from .forms import UserRegistrationForm,  UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile

# @login_required
# def profile(request):
#     user = request.user
#     if request.method == 'POST':
#         my_object = Profile.objects.get(user)
#         form = ProfileUpdateForm(request.POST, instance = my_object)    
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Your Profile has been Updated!')
#             return redirect('login')
#     else:
#         form = ProfileUpdateForm()
        
#     context = {
#         'form' : form,
#         'username' : user
#     }
#     return render(request, 'users/profile.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        print(u_form)
        if u_form.is_valid():
            # print(u_form.cleaned_data)
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
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
            
