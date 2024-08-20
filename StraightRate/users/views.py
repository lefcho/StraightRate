from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm, ViewUserProfileForm
from ..reviews.models import VideoGameReview, MovieReview


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'users/create-user.html', {'form': form})


@login_required
def view_profile(request):
    user = request.user
    movie_reviews = MovieReview.objects.filter(user=user)
    video_game_reviews = VideoGameReview.objects.filter(user=user)

    # Handle profile update
    if request.method == 'POST' and 'profile_update' in request.POST:
        form = ViewUserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('view-profile')
    else:
        form = ViewUserProfileForm(instance=user)

    context = {
        'form': form,
        'movie_reviews': movie_reviews,
        'video_game_reviews': video_game_reviews,
    }
    return render(request, 'users/view-profile.html', context)


