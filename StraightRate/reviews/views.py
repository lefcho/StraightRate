from django.db.models import Avg
from django.shortcuts import render, get_object_or_404

from StraightRate.reviews.models import Movie, VideoGame


def home(request):
    top_movies = (Movie.objects
                  .annotate(avg_rating=Avg('reviews__rating'))
                  .order_by('-avg_rating')
    [:5])
    top_games = (VideoGame.objects
                 .annotate(avg_rating=Avg('reviews__rating'))
                 .order_by('-avg_rating')
    [:5])
    context = {
        'top_movies': top_movies,
        'top_games': top_games,
    }

    return render(request, 'common/home.html', context)


def details_movie_view(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.reviews.all()

    context = {
        'movie': movie,
        'reviews': reviews,
    }
    return render(request, 'movies/movie-details.html', context)
