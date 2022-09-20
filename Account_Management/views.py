from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    form = UserCreationForm()
    registered = False

    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            form.save()

            registered = True

    return render(request, 'Account_Management/signup.html', {'form': form, 'registered': registered})
