from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import RegistrationForm, UpdateUserForm, UpdateUserProfileForm

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return redirect('home')
    else:
        registration_form = RegistrationForm()
    return render(request, 'users/registration.html', {'registration_form': registration_form})

@login_required
def user_profile(request):
    return render(request, 'users/user_profile.html')

@login_required
def user_profile_edit(request):
    
    if request.method == 'POST':
        update_user_form = UpdateUserForm(request.POST, instance=request.user)
        update_user_profile_form = UpdateUserProfileForm(request.POST, request.FILES, 
                                                         instance=request.user.userprofile)
        if update_user_form.is_valid() and update_user_profile_form.is_valid():
            update_user_form.save()
            update_user_profile_form.save()
            return redirect('user-profile')
    else:
        update_user_form = UpdateUserForm(instance=request.user)
        update_user_profile_form = UpdateUserProfileForm(instance=request.user.userprofile)
    
    forms = {'update_user_form': update_user_form, 'update_user_profile_form': update_user_profile_form}

    return render(request, 'users/user_profile_edit.html', forms)