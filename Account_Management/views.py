from django.shortcuts import render
from .forms import SignupForm, EditUserProfileForm, ProfilePictureForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# sign up or create user account
def signup(request):
    form = SignupForm()
    registered = False

    if request.method == 'POST':
        form = SignupForm(data=request.POST)

        if form.is_valid():
            form.save()

            registered = True

    return render(request, 'Account_Management/signup.html', {'form': form, 'registered': registered})


# account signin or login system 
def signin(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

    return render(request, 'Account_Management/signin.html', {'form': form})


# account signout or logout system 
@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# show user profile
@login_required
def user_profile(request):
    return render(request, 'Account_Management/user_profile.html')


# change user information
@login_required
def edit_user_profile(request):
    current_user = request.user

    form = EditUserProfileForm(instance=current_user)

    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, instance=current_user)

        if form.is_valid():
            form.save()

            form = EditUserProfileForm(instance=current_user)

    return render(request, 'Account_Management/edit_user_profile.html', {'form': form})


# change user login password
@login_required
def change_password(request):
    current_user = request.user

    changed = False

    form = PasswordChangeForm(current_user)

    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)

        if form.is_valid():
            form.save()

            changed = True

    return render(request, 'Account_Management/change_password.html', {'form': form, 'changed': changed})


# add user profile picture 
@login_required
def add_profile_picture(request):
    form = ProfilePictureForm()

    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)

        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('Account_Management_App:user_profile'))

    return render(request, 'Account_Management/add_profile_picture.html', {'form': form})


# change user profile picture 
@login_required
def change_profile_picture(request):
    form = ProfilePictureForm(instance=request.user.user_profile)

    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user.user_profile)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Account_Management_App:user_profile'))

    return render(request, 'Account_Management/add_profile_picture.html', {'form': form})