from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

def profile_view(request):
    return render(request, 'profile.html')

def game_view(request):
    return render(request, 'game.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def forgot_pass_view(request):
    return render(request, 'forgotpass.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Succesfully")
            return redirect('login_view')

    else:
        form = UserRegistrationForm()

    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                if not remember_me:
                    request.session.set_expiry(0)
                return redirect('dashboard')
            
            else:
                return render(request, 'login.html', {'error': 'Invalid login credentials. Please try again.'})
                # messages.error(request, 'Invalid login credentials. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'loginform':form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login_view')
