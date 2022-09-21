from django.shortcuts import render
from .forms import SignupForm


def signup(request):
    form = SignupForm()
    registered = False

    if request.method == 'POST':
        form = SignupForm(data=request.POST)

        if form.is_valid():
            form.save()

            registered = True

    return render(request, 'Account_Management/signup.html', {'form': form, 'registered': registered})
