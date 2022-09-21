from django.shortcuts import render
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


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