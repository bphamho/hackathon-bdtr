from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import RegistrationForm



# Create your views here.
def register_user(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
    else:
        registration_form = RegistrationForm()
    return render(request, 'users/registration.html', {'registration_form': registration_form})

@login_required
def user_profile(request):
    return render(request, 'users/user_profile.html')

def home(request):
    return render(request, 'users/home.html')
