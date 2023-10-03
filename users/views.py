from rest_framework import generics
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.contrib import messages
from .serializers import UserSerializer


# class register(generics.ListCreateAPIView):
#     serializer_class = UserSerializer

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             # user = form.save()  # Save the User instance
#             # user_profile = form.instance  # Access the related UserProfile instance
#             # user_profile.user = user
#             # user_profile.save()
#             # # Redirect to a thank you page or login page
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()

#     return render(request, 'users/register.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)    
        if form.is_valid():
            user = form.save()  # Save the User instance
            login(request, user)
            messages.success(request, f'Your Account has been created! You can now Log in')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form' : form})
            
            
            
            
            # user = UserProfile (
            #     first_name = request.form.get('first_name'),
            #     last_name = request.form.get('last_name'),
            #     username = request.form.get('username'),
            #     DateOfBirth = request.form.get('DateOfBirth'),
            #     gender = request.form.get('gender'),
            #     email = request.form.get('email'),
            #     PhoneNo = request.form.get('PhoneNo'),
            # )