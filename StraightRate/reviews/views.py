from django.shortcuts import render

from StraightRate.reviews.models import Movie, VideoGame


def home(request):
    top_movies = Movie.objects.all()
    top_games = VideoGame.objects.all()

    context = {
        'top_movies': top_movies,
        'top_games': top_games,
    }

    return render(request, 'common/home.html', context)