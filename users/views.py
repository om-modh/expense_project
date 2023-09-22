from rest_framework import generics
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from .serializers import UserSerializer

class register(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    def register(request):
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)    
            if form.is_valid():
                form.save()
                messages.success(request, f'Your Account has been created! You can now Log in')
                return redirect('login')
        else:
            form = UserRegistrationForm()
        return render(request, 'users/register.html', {'form' : form})