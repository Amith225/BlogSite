from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Profile


def update_user_data(user):
    Profile.objects.update_or_create(user=user, defaults={'email': user.profile.email,},)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            # email info
            Profile.objects.create(user=user)
            user.profile.email = form.cleaned_data.get('email')
            update_user_data(user)

            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
